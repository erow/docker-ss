import os
env=os.environ
#env={'port':3128,'crypt':'as','key':'as','mode':'fast','remote':'111'}
print(env)
port=env['export']

kcp_cfg="""{
"target":"127.0.0.1:8388",
"mtu": 1450,
"sndwnd": 876,
"rcvwnd": 876,
"datashard": 90,
"parityshard": 10,
"""+\
'"listen": "0.0.0.0:{0},"\n'.format(port)+\
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
f=open('kcp_ss.json','w')
f.write(kcp_cfg)


kcp_cfg="""{
"localaddr":"0.0.0.0:8388",
"mtu": 1450,
"sndwnd": 876,
"rcvwnd": 876,
"datashard": 90,
"parityshard": 10,
"""+\
"\"mode\": \"{0}\",\n\"crypt\":\"{1}\",\n\"key\":\"{2}\","\
    .format(env['mode'],env['crypt'],env['key'])\
+'"\nremoteaddr": "{0}:{1}",'.format(env['remote'],port)\
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
"""+\
"\"password\": \"{0}\",".format(env['key'])+\
"""
"method": "aes-256-cfb"
}
"""
f=open('ss.json','w')
f.write(ss_cfg)

