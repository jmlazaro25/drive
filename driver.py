from direct.showbase.ShowBase import ShowBase

from panda3d.core import CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionTube, CollisionNode
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import Vec4, Vec3
from panda3d.core import WindowProperties

from sim_objs import Car

class Sim(ShowBase):
    def __init__(self, light_vec: tuple[float] = (45.0, -45.0, 0.0)):
        ShowBase.__init__(self)

        #self.disableMouse()

        #properties = WindowProperties()
        #properties.setSize(1000, 750)
        #self.win.requestProperties(properties)

        mainLight = DirectionalLight("main light")
        self.mainLightNodePath = render.attachNewNode(mainLight)
        self.mainLightNodePath.setHpr(light_vec)
        render.setLight(self.mainLightNodePath)

        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(self.ambientLightNodePath)

        #render.setShaderAuto()

        #self.environment = loader.loadModel("Models/Misc/environment")
        #self.environment.reparentTo(render)

        self.pusher = CollisionHandlerPusher()
        self.cTrav = CollisionTraverser()

        self.updateTask = taskMgr.add(self.update, "update")

        self.player = Car(
            Vec3(0.0, 0.0, Car.def_height/2.0),
            0.0,
            Vec3(0.0, 0.0, 0.0),
            'player'
        )
        other = Car(
            Vec3(0.0, 0.0, 10.0),
            45.0,
            Vec3(0.0, 0.0, 0.0),
            'other'
        )

        self.camera.set_pos(self.player.model.get_pos())
        self.camera.set_h(self.player.heading)

    def update(self, task):
        self.player.update()
        print(self.player.model.get_pos())
        return task.cont


sim = Sim()
sim.run()
