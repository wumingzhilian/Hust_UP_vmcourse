#! /bin/sh
if [ -z "$(grep '^ctf:' /etc/passwd)" ]; then
  groupadd -r ctf && useradd -r -g ctf ctf
fi
if [ -d /ctf ]; then
  mkdir -p /home/
  mv /ctf /home
  mv /home/ctf/flag /
fi

touch /var/log/xinted.log
xinetd -f /etc/xinetd.d/ctf && tail -f /var/log/xinted.log
