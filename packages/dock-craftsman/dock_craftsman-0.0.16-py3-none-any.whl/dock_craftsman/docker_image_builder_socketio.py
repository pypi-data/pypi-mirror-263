import docker
from .utils import generate_unique_docker_image_name

class DockerImageBuilderSocketio:
    def __init__(self, docker_socket=None, socketio=None, socketio_room= None):
        self.image_name = generate_unique_docker_image_name()
        self.dockerfile_content = None
        self.dockerfile = None
        self.path = '.'
        self.tags = 'latest'
        self.build_args = {}
        self.platform = None
        self.cache_from = None
        self.extra_hosts = None
        self.client_error = False
        self.socketio = socketio
        self.socketio_room = socketio_room
        
        try:
            if docker_socket:
                self.docker_client = docker.DockerClient(base_url=docker_socket)
            else:
                self.docker_client = docker.from_env()
            
            if self.socketio:
                self.emit('Docker client initialized successfully', 'text', 'green')
        except Exception as e:
            if self.socketio:
                self.emit(str(e), 'text', 'red')
            self.client_error = True

    def emit(self, message, message_type, color):
        if self.socketio:
            self.socketio.emit('message', {'message': message, 'type': message_type, 'color': color}, to=self.socketio_room)

    def set_name(self, image_name):
        self.image_name = image_name
        return self

    def set_tag(self, tags):
        self.tags = tags
        return self

    def set_content(self, dockerfile_content):
        self.dockerfile_content = dockerfile_content
        
        # Define the polyfill
        # source: https://github.com/docker/docker-py/issues/2105#issuecomment-613685891
        docker.api.build.process_dockerfile = lambda dockerfile, path: ('Dockerfile', dockerfile)
        
        return self
    
    def set_dockerfile(self, docker_file):
        self.dockerfile = docker_file
        return self
    
    def set_path(self, path):
        self.path = path
        return self

    def set_build_args(self, build_args):
        self.build_args = build_args
        return self

    def set_platform(self, platform):
        self.platform = platform
        return self

    def set_cache_from(self, cache_from):
        self.cache_from = cache_from
        return self

    def set_extra_hosts(self, extra_hosts):
        self.extra_hosts = extra_hosts
        return self

    def build(self):
        if self.client_error:
            return False
        
        import time

        start_time = time.time()  # Record the start time

        dockerfile_content = self.dockerfile_content

        build_params = {
            'tag': f'{self.image_name}:{str(self.tags)}',
            'buildargs': self.build_args,
            'platform': self.platform,
            'cache_from': self.cache_from,
            'extra_hosts': self.extra_hosts,
            'path': self.path,
            'pull': False,
            'nocache': False,
        }
        
        if self.dockerfile_content is not None:
            build_params.update({'dockerfile': self.dockerfile_content})
        
        if self.dockerfile is not None:
            build_params.update({'dockerfile': self.dockerfile})

        build_params = {k: v for k, v in build_params.items() if v is not None}

        try:
            response = self.docker_client.api.build(**build_params, decode=True, forcerm=True, rm=True)

            image_id = None
            is_using_cache = False
            self.emit(f'base image downloading', 'text', 'blue')

            for chunk in response:
                if 'errorDetail' in chunk:
                    error_detail = chunk['errorDetail']
                    self.emit(error_detail['message'], 'text', 'red')
                    return False

                if 'stream' in chunk:
                    step_output = chunk['stream'].strip()

                    if "Using cache" in step_output:
                        is_using_cache = True
                    elif "Step" in step_output:
                        cached_msg = 'CACHED ' if is_using_cache else ''
                        original_string = step_output[5:]
                        modified_string = f"[{original_string.split(':')[0].strip()}] {original_string.split(':', 1)[1].strip()}"
                        self.emit(f'=> {cached_msg} {modified_string}', 'text', 'blue')
                        is_using_cache = False
                    elif "Successfully built" in step_output:
                        parts = step_output.split()
                        if len(parts) == 3:
                            image_id = parts[2]
                            break
                    elif "[Warning] The requested image's platform (linux/amd64)" in step_output:
                        pass
                    else:
                        self.emit(step_output, 'text', 'yellow')
            if image_id:
                message = (
                    f"Build Successful\n\n"
                    f"Image Name: {self.image_name}\n"
                    f"Image Tag: {self.tags or 'latest'}"
                )
                self.emit(message, 'panel', 'green')
                end_time = time.time()
                total_time = end_time - start_time
                total_time_minutes = total_time / 60
                self.emit(f'Total Execution Time: {total_time_minutes:.2f} minutes', 'text', 'green')
                return True
            else:
                self.emit('Build failed: Unable to retrieve image ID', 'text', 'red')
                return False

        except docker.errors.BuildError as e:
            self.emit(f'Docker build failed: {e}', 'text', 'red')
            return False
        except docker.errors.APIError as e:
            self.emit(f'Docker API error: {e}', 'text', 'red')
            return False
        except Exception as e:
            self.emit(f'An unexpected error occurred during build: {e}', 'text', 'red')
            self.emit(f'Exception type: {type(e).__name__}', 'text', 'red')
            return False
