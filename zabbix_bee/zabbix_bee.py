#coding:utf-8
import os,sys,getopt,ftplib,tarfile,ConfigParser,re
reload(sys)
sys.setdefaultencoding('utf8')

class QywpProcess:
    global results_list,local_ip

    def __init__(self,name):
        self.plugins=[]
        self.name=name
        self.__loadPlugins(name)

    def __loadPlugins(self,name):
        checkPath=os.path.split(os.path.realpath(__file__))[0]
        if os.path.exists(checkPath+'/plugins/'+self.name):
            for filename in os.listdir(checkPath+'/plugins/'+self.name):
                if not filename.endswith('.py') or filename.startswith('_'):
                    continue
                self.__runPlugins(filename,name)
        else:
            print "[*] Plugins directory not in here!"
            print "[*] Done."

    def __runPlugins(self,filename,name):
        plugins_name=os.path.splitext(filename)[0]
        plugin=__import__('plugins.'+self.name+'.'+plugins_name,fromlist=[plugins_name])
        clazz=plugin.getPluginClass()
        o=clazz()
        zabbix_Key=o.getKey()
        zabbix_status=o.getStatus()
        print "[ %s ]:key----- %s\t status-----%s" % (clazz,zabbix_Key,zabbix_status)
        query="zabbix_sender -c /etc/zabbix/zabbix_agentd.conf  -k %s -o %s" % (zabbix_Key,zabbix_status)
        print query
        os.system(query)
        self.plugins.append(o)

if __name__=="__main__":
    global username,mode
    username=""
    mode=""
    try:
		options,args=getopt.getopt(sys.argv[1:],"hdn:m:",["help","name=","mod="])
    except getopt.GetoptError:
        print_read()
        sys.exit()
    for name,value in options:
        if name in ("-h","--help"):
            sys.exit(1)
        if name in ("-d"):
            obj=QywpProcess('dection')
