# Python actors library

# Usage
	from pactors.core import Actor
	
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

# License

	This software is licensed under the BSD License. See the license file in the top distribution directory for the full license text.
