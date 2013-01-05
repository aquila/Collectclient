""" type help(Collect) """
import zmq
import json
import time

class CollectorException(Exception):
  def __init__(self, expr, msg):
    self.expr=expr
    self.msg=msg
  
  def __str__(self):
    return "%s: %s"%(self.expr,self.msg)
  
class Collector:
  """ Connects to the collector and writes data 
  use::
   c=Collect(test="dummy",resource="address",id="127.0.0.1",host="127.0.0.1",port=25500)
   c.write("FOO")
   c.writemany(["Foo","bar","baz"])
   """
  def __init__(self,test=None,resource=None,id=None,host="127.0.0.1",port=25500):
    if not (test and resource and id):
      raise CollectorException("Not properly initialized", """Needs test, resource and id """)
      
    self.test=test
    self.resource=resource
    self.id=id
    context=zmq.Context()
    self.sender=context.socket(zmq.PUSH)
    self.sender.connect("tcp://%s:%s"%(host,port))

  def write(self,data):
    message={"timestamp":int(time.time()),
      self.resource:self.id,
      "test":self.test,
      "data":data}
    self.sender.send(json.dumps(message))

  def writemany(self,data):
    for d in data:
      self.write(d)
