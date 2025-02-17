# Docker Hub Image Push Script

This Python script automates the process of tagging and pushing Docker images to Docker Hub. It simplifies the workflow for managing multiple images with consistent tagging. Use it if you are not using ci-cd in inditail building time.

## Features
- Logs in to Docker Hub using the specified username.
- Tags Docker images with a specified version tag.
- Pushes tagged images to Docker Hub.
- Handles errors gracefully and provides clear feedback.

## Prerequisites
1. Ensure you have Python 3 installed.
2. Docker must be installed and configured on your system.
3. Your Docker images must be built and available locally (`docker images`).

## Setup
1. Clone this repository.
   ```bash
   git clone <repository-url>
  or
Use just copy dockerhub_push.py to your docker image directory and run it.

## How to use
1. Make reposotories for this in docker hub.
2. Add your username in the string ,DOCKER_USER = "username".
3. Add id of images as key and thier name as value.
4. If all images have same tagname go for 2nd approach. If not got for fist approach and add thier tag names in a correct order in the array ,tag_version = ["v1.0.0","v1.0.2"].
5. If your approach is first ,cmd down this part {tag = f"{DOCKER_USER}/{repo_name}:{tag_version}"}, and uncmd the first approach. Or go with the second.
6. Then run the cmd using "python -m dockerhub_push.py", give password to your dockerhub and you are good to go.
