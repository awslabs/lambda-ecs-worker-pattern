# Constants (User configurable)

FULL_NAME_AND_EMAIL = 'Peter Lepeska <peter.lepeska@viasat.com>'  # For Dockerfile/POV-Ray builds.
APP_NAME = 'ecs-test-plepeska'  # Used to generate derivative names unique to the application.

# create a repo here https://console.aws.amazon.com/ecs/home?region=us-east-1#/repositories
# DOCKERHUB_USER will be created as part of that
DOCKERHUB_USER = '831754492748.dkr.ecr.us-east-1.amazonaws.com'
DOCKERHUB_EMAIL = 'email@domain.com'
DOCKERHUB_REPO = 'ecs-test'
DOCKERHUB_TAG = DOCKERHUB_USER + '/' + DOCKERHUB_REPO + ':' + APP_NAME

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'default'  # The same profile used by your AWS CLI installation

SSH_KEY_NAME = 'automation.pem'  # Expected to be in ~/.ssh
ECS_CLUSTER = 'peter'
