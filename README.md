# Script changes labels/image values in yaml files. 
#
### Usage: 
###### python3 blue-green-changer.py -f [list of yaml files to amend] -i [new_docker_image] -v [version label key --default is 'role']
###### ex. 
###### python3 blue-green-changer.py -f deployment.yaml service.yaml -i dockerhub/superimage:latest

