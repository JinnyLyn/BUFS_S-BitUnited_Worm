FROM ubuntu:22.04@sha256:2b7412e6465c3c7fc5bb21d3e6f1917c167358449fecac8176c6e496e5c1f05f

ENV user bof
ENV chall_port 31337

RUN apt-get update
RUN apt-get -y install socat

RUN adduser $user

ADD ./deploy/flag /home/$user/flag
ADD ./deploy/$user /home/$user/$user
ADD ./deploy/cat /home/$user/cat

RUN chown root:$user /home/$user/flag
RUN chown root:$user /home/$user/$user
RUN chown root:$user /home/$user/cat

RUN chmod 755 /home/$user/$user
RUN chmod 440 /home/$user/flag
RUN chmod 440 /home/$user/cat

WORKDIR /home/$user
USER $user
EXPOSE $chall_port
CMD socat -T 60 TCP-LISTEN:$chall_port,reuseaddr,fork EXEC:/home/$user/$user
