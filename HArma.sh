#!/bin/bash

pname="$1"
cmd="$2"

function reload
{
  pid=`cat var/$pname.pid`
  kill -28 $pid
  echo "$pname reloaded (pid: $pid)"
}

function restart
{
  stop
  start
}

function start
{
  pushd ./src >/dev/null 2>&1
  nohup ./helper.py $rpath $pname >../var/$pname.nohup.out 2>/dev/null &
  pid=$!
  popd >/dev/null 2>&1
  if [ -d /proc/$pid ]; then
    echo "$pname started (pid: $pid)"
    echo $pid > var/$pname.pid
  else
    echo "$pname failed to start"
  fi
}

function stop
{
  kill -2 `cat var/$pname.pid`
  if [ -d /proc/$pid ]; then
    echo "$pname stopped"
    rm var/$pname.pid
  else
    echo "$pname failed to stop"
  fi
}

function status
{
  if [ -e var/$pname.pid ]; then
    echo "$pname is running"
  else
    echo "$pname is not running"
  fi
}

function usage
{
  echo "Usage: $0 [coordinator|courier|priest|vampire|zealot] [reload|restart|start|stop|status]"
  exit
}

if [[ "$pname" = "" ]]; then
  usage
elif [[ "$pname" = "coordinator" ]]; then
  rpath="depth"
elif [[ "$pname" = "courier" ]]; then
  rpath="depth"
elif [[ "$pname" = "priest" ]]; then
  rpath="depth"
elif [[ "$pname" = "vampire" ]]; then
  rpath="depth"
elif [[ "$pname" = "zealot" ]]; then
  rpath="depth"
else
  usage
fi

if [[ "$cmd" = "" ]]; then
  status
elif [[ "$cmd" = "reload" ]]; then
  reload
elif [[ "$cmd" = "restart" ]]; then
  restart
elif [[ "$cmd" = "start" ]]; then
  start
elif [[ "$cmd" = "stop" ]]; then
  stop
elif [[ "$cmd" = "status" ]]; then
  status
else
  usage
fi

