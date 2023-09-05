from panda3d.core import CollisionNode, CollisionBox
from panda3d.core import Vec3


C_FRICTION = 10.0


class Car():
    def_width = 2.0
    def_length = 5.0
    def_height = 2.0
    def_mass = 1600.0
    def_max_speed = 50.0
    def_max_accel = 10.0
    def_max_break = 10.0

    def __init__(
            self,
            pos,
            heading,
            speed,
            collider_name,
            width: float = def_width,
            length: float = def_length,
            height: float = def_height,
            mass: float = def_mass,
            color: tuple[float] = (0.0, 0.0, 0.0),
            max_speed: float = def_max_speed,
            max_accel: float = def_max_accel,
            max_break: float = def_max_break
        ):
        self.heading = heading
        self.speed = speed
        self.max_speed = 100.0
        self.weight = mass * 9.81
        self.color = color
        self.max_speed = max_speed
        self.max_accel = max_accel
        self.max_break = max_break

        self.model = loader.load_model('box.egg')
        self.model.reparent_to(render)
        self.model.set_pos(pos)
        self.model.set_hpr(self.heading, 0.0, 0.0)

        colliderNode = CollisionNode(collider_name)
        colliderNode.addSolid(
            CollisionBox((-width/2, -length/2, 0), (width/2, length/2, height))
        )
        self.collider = self.model.attachNewNode(colliderNode)
        self.collider.setPythonTag("owner", self)

    def update(self):
        self.model.set_pos(self.model.get_pos() + Vec3(0.0, 0.0, 0.001))
        """
        speed = self.velocity.length()
        if speed > self.maxSpeed:
            self.velocity.normalize()
            self.velocity *= self.maxSpeed
            speed = self.maxSpeed

        if not self.walking:
            frictionVal = C_FRICTION*dt
            if frictionVal > speed:
                self.velocity.set(0, 0, 0)
            else:
                frictionVec = -self.velocity
                frictionVec.normalize()
                frictionVec *= frictionVal

                self.velocity += frictionVec

        self.actor.setPos(self.actor.getPos() + self.velocity*dt)
        """
