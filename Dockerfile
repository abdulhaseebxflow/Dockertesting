FROM abdulhaseebxflow/docker:calendar

RUN apt -y update && apt -y upgrade && apt install -y ssh && apt install -y python2.7

EXPOSE 22

CMD ["/bin/bash","-D"]
