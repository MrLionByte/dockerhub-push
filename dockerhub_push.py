import subprocess

#Add Your docker-hub username
DOCKER_USER = "username" 

#add image with image id as key and service name as value 
IMAGES = {
    "eee0bcd942df": "user_auth",
    "exampleid2": "example_image_name_2",
    "exampleid3": "example_image_name_3",
}

print("Logging in to Docker Hub...")
subprocess.run(["docker", "login", "-u", DOCKER_USER], check=True)

# 1st Approach
# tag_version = ["v1.2.0","v1.0.0","v1.2.0"]

# 2nd Approach
 tag_version = "v1.2.0"

# If 1st approach is being used use this for correct tagging with index
tag_index = 0


for image_id, repo_name in IMAGES.items():
    #1st Approach  
    # tag = f"{DOCKER_USER}/{repo_name}:{tag_version[tag_index]}"
    # tag_index += 1    
    
    #2nd Approach
    tag = f"{DOCKER_USER}/{repo_name}:{tag_version}"
    
    print(f"Tagging image {image_id} as {tag}...")
    subprocess.run(["docker", "tag", image_id, tag], check=True)
    
    print(f"Pushing {tag} to Docker Hub...")
    subprocess.run(["docker", "push", tag], check=True)

print("All images have been pushed to Docker Hub!")
