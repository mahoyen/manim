from manimlib.imports import *

class DotMovement(Scene):

    def construct(self):
        dotlist = []
        nDots = 3
        colorlist  = [BLUE, RED, GREEN]
        positionlist = [ORIGIN, UP, DOWN]
        for i in range(nDots):
            dotlist.append(Dot(positionlist[i], color=colorlist[i]))
        self.add(*dotlist)
        self.play(
            Indicate(dotlist[1])
        )
        self.wait()

        # dotlist[1].target = Dot(LEFT, color=PURPLE)
        x_trans, y_trans, z_trans  = -5, 2, 0
        theta = np.deg2rad(40)
        

        def apply_rotTransMatrix(x, y, z, t):
            rotTransMatrix = np.array(
            [[np.cos(theta), -np.sin(theta), 0, t*x_trans],
             [np.sin(theta),  np.cos(theta), 0, t*y_trans],
             [            0,              0, 1, t*z_trans]]
        )
            vector = np.array([x, y, z, 1])
            return np.matmul(rotTransMatrix, vector)


        #dotlist[1].apply_function(lambda x: apply_rotTransMatrix(*x, rotTransMatrix))
        self.play(
            Homotopy(apply_rotTransMatrix, dotlist[0])
        )
        self.wait(5)