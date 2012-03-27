from gevent import monkey
monkey.patch_all()
import gevent
from gevent import Greenlet
from gevent.queue import Queue


class MetaActor(type):
	def __new__(meta, classname, supers, classdict):
		cls = type.__new__(meta, classname, supers, classdict)
		cls.actors = []
		return cls


class Actor(Greenlet):
	__metaclass__ = MetaActor
	
	def __init__(self):
		Greenlet.__init__(self)
		self.inbox = Queue()
		Actor.actors.append(self)
		
	def send(self, actor, message):
		actor.inbox.put(message)
		
	def receive(self, message):
		raise NotImplemented()
		
	@staticmethod
	def wait_actors():
		gevent.joinall(Actor.actors)
		
	def loop(self):
		if not self.inbox.empty():
			self.receive(self.inbox.get())
		gevent.sleep()
		
	def _run(self):
		while self.started:
			self.loop()

if __name__ == "__main__":			
	class MyActor(Actor):
		def __init__(self, name):
			self.name = name
			super(MyActor, self).__init__()
		
		def receive(self, message):
			print "%s received: %s" % (self.name, message)
			self.kill()

	
	a1 = MyActor("actor1")
	a1.start()
	a2 = MyActor("actor2")
	a2.start()
	a1.send(a2, {"sender": a1, "msg": "hi)"})
	a2.send(a1, "hello")
	Actor.wait_actors()

		

