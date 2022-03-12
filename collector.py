from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
import time, os, subprocess
import sys
import shutil
import datetime, requests, bs4, re
from datetime import timedelta
from bs4 import BeautifulSoup
from subprocess import Popen, PIPE
import logging

fo, server_load, cpu_usage, access_count, idle_c,serv_up_w,current_w,load_1,load_2,s = 0.0,0.0, 0.0, 0.0, 0.0, 0.0,0.0,0.0,0.0,0.0




def server_status():

    try:
        args = ['apachectl', 'configtest']

        result = Popen(args, stdout=PIPE, stderr=PIPE).communicate()

        if (re.search("Syntax OK", result[1].decode('utf-8'))):
            s = 1.0
        else:
            s = 0.0

        res = requests.get("http://localhost/server-status", headers={'Accept': 'application/json'}, verify=False)
        b = []
        soup = BeautifulSoup(res.text)
        for node in soup.findAll('dt'):
            b.append(''.join(node.findAll(text=True)))
        sd, sh, sm, ss = 0, 0, 0, 0
        serv=""
        for i in b:
            if (re.search("^Total accesses", i)):
                access = i.split(':')[1].split(" ")[1]
            if (re.search("^CPU Usage", i)):
                usage = i.split('-')[1].split("%")[0]
            if (re.search("^Server load", i)):
                load = i.split(':')[1].split(" ")[1]
            if (re.search("requests/sec", i)):
                req = i.split(' ')[0]
            if (re.search("idle workers", i)):
                idle = i.split(' ')[-3]
            if (re.search("idle workers", i)):
                current = i.split(' ')[0]
            if (re.search("^Server load", i)):
                load1 = i.split(':')[1].split(" ")[-2]
            if (re.search("^Server load", i)):
                load2 = i.split(':')[1].split(" ")[-1]

            try:


                if (re.search("Server uptime", i)):
                    serv = i.split(':')[1]

                if (re.search("day", serv) and re.search("hour", serv) and re.search("minute", serv) and re.search("second",
                                                                                                                   serv)):
                    sdhm = serv.split(" ")
                    sd = sdhm[2]
                    sh = sdhm[4]
                    sm = sdhm[6]
                    ss = sdhm[8]
                    sd = int(sd)
                    sh = int(sh)
                    sm = int(sm)
                    ss = int(ss)
                elif (re.search("day", serv) and re.search("minute", serv) and re.search("second", serv)):
                    sdhm = serv.split(" ")
                    sd = sdhm[2]
                    sm = sdhm[4]
                    ss = sdhm[6]
                    sd = int(sd)
                    sm = int(sm)
                    ss = int(ss)
                elif (re.search("day", serv) and re.search("hour", serv) and re.search("second", serv)):
                    sdhm = serv.split(" ")
                    sd = sdhm[2]
                    sh = sdhm[4]
                    ss = sdhm[6]
                    sd = int(sd)
                    sh = int(sh)
                    ss = int(ss)

                elif (re.search("day", serv) and re.search("second", serv)):
                    sdhm = serv.split(" ")
                    sd = sdhm[2]
                    ss = sdhm[4]
                    sd = int(sd)
                    ss = int(ss)

                elif (re.search("hour", serv) and re.search("minute", serv) and re.search("second", serv)):
                    sdhm = serv.split(" ")
                    sh = sdhm[2]
                    sm = sdhm[4]
                    ss = sdhm[6]
                    sh = int(sh)
                    sm = int(sm)
                    ss = int(ss)
                elif (re.search("hour", serv) and re.search("second", serv)):
                    sdhm = serv.split(" ")
                    sh = sdhm[2]
                    ss = sdhm[4]
                    sh = int(sh)
                    ss = int(ss)

                elif (re.search("minute", serv) and re.search("second", serv)):
                    sdhm = serv.split(" ")
                    sm = sdhm[2]
                    ss = sdhm[4]
                    sm = int(sm)
                    ss = int(ss)
                elif (re.search("second", serv)):
                    sdhm = serv.split(" ")
                    ss = sdhm[-2]
                    ss = int(ss)

                sd = int(sd)
                sh = int(sh)
                sm = int(sm)
                ss = int(ss)

                # Define the constants
                SECONDS_PER_MINUTE = 60
                SECONDS_PER_HOUR = 3600
                SECONDS_PER_DAY = 86400

                # Read the inputs from user
                days = sd
                hours = sh
                minutes = sm
                seconds = ss

                # Calculate the days, hours, minutes and seconds
                total_seconds = days * SECONDS_PER_DAY
                total_seconds = total_seconds + (hours * SECONDS_PER_HOUR)
                total_seconds = total_seconds + (minutes * SECONDS_PER_MINUTE)
                total_seconds = total_seconds + seconds
                serv_up = total_seconds
            except:
                serv_up=0.0

        load_1 = float(load1)
        load_2 =float(load2)
        serv_up_w=float(serv_up)
        current_w=float(current)
        idle_c = float(idle)
        req_s = float(req)
        server_load = float(load)
        cpu_usage = float(usage)*100
        access_count = float(access)
    except:
        req_s, server_load, cpu_usage, access_count, idle_c,serv_up_w,current_w,load_1,load_2,s = 0.0,0.0,0.0, 0.0, 0.0, 0.0, 0.0,0.0,0.0,0.0

    try:
        output = subprocess.check_output(
            "curl -s -k --max-time 5 localhost:80 -s -o -I -w '%{http_code}'",
            shell=True).decode('utf-8')
    except:
        output = "400"
    if output == "200":
        f = 1.0
    else:
        f = 0.0



    return f, server_load, cpu_usage, access_count, idle_c,serv_up_w,current_w,req_s,load_1,load_2,s


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        global fo
        global server_load
        global cpu_usage
        global access_count
        global idle_c
        global serv_up_w
        global current_w
        global s
        global req_s
        global load_1
        global load_2


        m = datetime.datetime.now().minute

        n = datetime.datetime.now().second

        f, server_load, cpu_usage, access_count, idle_c,serv_up_w,current_w,req_s,load_1,load_2,s = server_status()

        fo, server_load, cpu_usage, access_count, idle_c,serv_up_w,current_w,req_s,load_1,load_2,s = float(f), float(server_load), float(cpu_usage), float(
                access_count), float(idle_c),float(serv_up_w),float(current_w),float(req_s),float(load_1),float(load_2),float(s)

        logging.basicConfig(filename='app.log', filemode='w',level=logging.DEBUG)
        logging.debug("TIME- {}, SERVER LOAD- {}, LOAD1- {}, LOAD2- {}, UP STATUS- {}, CPU USAGE- {}, ACCESS COUNT- {}, IDLE COUNT-{}, SERVER UPTIME- {}, CURRENT WORKER- {}, REQ/SEC- {}, CONFIGTEST- {}\n".format(
                datetime.datetime.now(), server_load, load_1, load_2, fo, cpu_usage, access_count, idle_c,
                serv_up_w, current_w, req_s, s))


        try:


            k = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            k.add_metric(["server_load"], server_load)
            yield k

            kk = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            kk.add_metric(["server_load_1"], load_1)
            yield kk

            kkk = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            kkk.add_metric(["server_load_2"], load_2)
            yield kkk

            i = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            i.add_metric(["up_status"], fo)
            yield i

            l = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            l.add_metric(["cpu_usage"], cpu_usage)
            yield l

            m = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            m.add_metric(["access_count"], access_count)
            yield m

            n = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            n.add_metric(["idle workers"], idle_c)
            yield n

            o = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            o.add_metric(["Server UP Time"], serv_up_w)
            yield o

            p = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            p.add_metric(["Current workers"], current_w)
            yield p

            q = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            q.add_metric(["Requests per sec"], req_s)
            yield q

            r = CounterMetricFamily("SERVER_STATUS", 'Help text', labels=['value', 'host'])
            r.add_metric(["Apache Config Test"], s)
            yield r



        except:
            pass


if __name__ == '__main__':

    start_http_server(9016)

    REGISTRY.register(CustomCollector())
    while True:

        time.sleep(30)

