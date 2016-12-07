import os
env=os.environ

port=3128

env['mode']=env['crypt']=env['key']=env['sskey']='***'
kcp_cfg="""{
"listen": "0.0.0.0:3128",
"target":"127.0.0.1:13121",
"mtu": 1450,
"sndwnd": 876,
"rcvwnd": 876,
"datashard": 90,
"parityshard": 10,
"""+\
"\"mode\": \"{0}\",\n\"crypt\":\"{1}\",\n\"key\":\"{2}\","\
    .format(env['mode'],env['crypt'],env['key'])\
+"""
"dscp": 46,
"nocomp": false,
"acknodelay": false,
"nodelay": 1,
"interval": 20,
"resend": 2,
"nc": 1,
"sockbuf": 4194304,
"keepalive": 10,
"log":"/log/kcp.log"
}"""
f=open('kcp_ss.json','w')
f.write(kcp_cfg)


kcp_cfg="""{
"localaddr":"0.0.0.0:12345",
"remoteaddr": " :12345",
"mtu": 1450,
"sndwnd": 876,
"rcvwnd": 876,
"datashard": 90,
"parityshard": 10,
"""+\
"\"mode\": \"{0}\",\n\"crypt\":\"{1}\",\n\"key\":\"{2}\","\
    .format(env['mode'],env['crypt'],env['key'])\
+"""
"dscp": 46,
"nocomp": false,
"acknodelay": false,
"nodelay": 1,
"interval": 20,
"resend": 2,
"nc": 1,
"sockbuf": 4194304,
"keepalive": 10
}"""
f=open('kcp_ss_client.json','w')
f.write(kcp_cfg)

##ss.json


ss_cfg=\
"""
{
"server": "127.0.0.1",
"server_port": 13121,
"""+\
"\"password\": \"{0}\",".format(env['sskey'])+\
"""
"method": "aes-256-cfb"
}
"""
f=open('ss.json','w')
f.write(ss_cfg)

