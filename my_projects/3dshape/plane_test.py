from manimlib.imports import *

alpha = -20*DEGREES

class Thing2(VectorScene):
    def construct(self):
        v_coords = np.array([4,3,0])
        self.add_axes(True)
        d1_offset = 1/3
        d2_offset = 2/3
        main_vector = Vector(direction=v_coords)
        dot1 = Dot(v_coords*d1_offset, color=YELLOW)
        dot2 = Dot(v_coords*d2_offset, color=YELLOW)
        slope = main_vector.get_slope()
        start_d1 = v_coords*(-10+d1_offset)
        stop_d1 = v_coords*(10+d1_offset)
        print(slope, start_d1, stop_d1)
        dashed_line1 = DashedLine(start = start_d1, end= stop_d1)
        self.add_vector(main_vector)
        self.play(ShowCreation(dot1))
        self.play(ShowCreation(dot2))
        self.play(Rotate(dashed_line1, angle=90*DEGREES))
        line1 = Line(start=ORIGIN, end=v_coords)

        self.play(Rotate(line1, angle=alpha, about_point=ORIGIN))
        b1 = dot1.get_y() - dot1.get_x()*dashed_line1.get_slope()
        x1 = b1/(line1.get_slope()-dashed_line1.get_slope())
        dot3pos = np.array([x1, line1.get_slope()*x1, 0])
        dot3 = Dot(dot3pos, color=RED)
        arc1to3 = ArcBetweenPoints(start = dot1.get_end(), end = dot3.get_end(), angle = alpha)
        self.play(ShowCreation(dot3))
        self.play(ShowCreation(arc1to3))

        """
        start_d2 = dashed_line1.get_start()
        stop_d2 = dashed_line1.get_end()
        dashed_line2 = DashedLine(start = start_d2, end= stop_d2)
        self.play(dashed_line2.move_to(dot2))"""
        self.wait(2)
        