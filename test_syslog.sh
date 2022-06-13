# echo "‘"<14>_sourcehost_ messagetext"’" | nc -v <host> <port>
echo "Input destination IP or hostname: "
read dest 
echo "Input destination port: "
read dest_port 
echo "<14>localhost testing syslog-ng" | nc -v dest dest_port
