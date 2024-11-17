import turtle
import math
import random
import time

class Asteroid:
    def __init__(self, size, x, y, speed=30, tilt=0):
        self.size = size
        self.tilt = tilt
        self.x = x
        self.y = y
        self.rs = random.uniform(-0.07, 0.07)
        self.speed = speed
        self.direction = random.uniform(0, 2*math.pi)
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.color("white")
        self.turtle.speed(0)
        self.s = []
        self.p = []
        for _ in range(12):
            self.s.append(random.uniform(0.5 * self.size, self.size))
    
    def draw_one(self, x, y):
        self.p.clear()
        self.turtle.up()
        px_first, py_first, angle = x + self.s[0] * math.cos(self.tilt), y + self.s[0] * math.sin(self.tilt), self.tilt
        self.p.append((px_first, py_first))
        self.turtle.goto(px_first, py_first)
        self.turtle.pendown()
        for i in range(11):
            angle += 2 * math.pi / 12
            px, py = x + self.s[i+1] * math.cos(angle), y + self.s[i+1] * math.sin(angle)
            self.turtle.goto(px, py)
        self.turtle.goto(px_first, py_first)
    
    def draw_two(self):
        if self.x > 300:
            self.x -= 600
        if self.y > 300:
            self.y -= 600
        if self.x < -300:
            self.x += 600
        if self.y < -300:
            self.y += 600
        self.turtle.clear()
        self.draw_one(self.x + 600, self.y)
        self.draw_one(self.x - 600, self.y)
        self.draw_one(self.x, self.y + 600)
        self.draw_one(self.x, self.y - 600)
        self.draw_one(self.x, self.y)
    
    def move(self, t):
        self.x += self.speed * t * math.cos(self.direction)
        self.y += self.speed * t * math.sin(self.direction)
        self.tilt -= self.rs

class Bullet:
    speed = 300  # Increased speed for better feel
    lifespan = 2.5

    def __init__(self, x, y, direction):
        self.x, self.y, self.direction = x, y, direction
        self.life = Bullet.lifespan
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.color("white")

    def draw(self):
        self.turtle.clear()
        if self.life >= 0:
            # Handle screen wrapping for bullets
            draw_positions = [
                (self.x, self.y),
                (self.x + 600, self.y),
                (self.x - 600, self.y),
                (self.x, self.y + 600),
                (self.x, self.y - 600)
            ]
            
            for pos in draw_positions:
                if -300 <= pos[0] <= 300 and -300 <= pos[1] <= 300:
                    self.turtle.goto(pos[0], pos[1])
                    self.turtle.dot(3)  # Made bullets slightly smaller

    def move(self, t):
        self.life = self.life - t
        dist = Bullet.speed * t
        
        # Update position
        self.x = self.x + dist * math.cos(self.direction)
        self.y = self.y + dist * math.sin(self.direction)
        
        # Handle screen wrapping
        if self.x > 300: self.x -= 600
        if self.x < -300: self.x += 600
        if self.y > 300: self.y -= 600
        if self.y < -300: self.y += 600

class Explosion:
    def __init__(self, x, y, screen2):
        self.x, self.y, self.p, self.dir, self.s, self.screen, self.t = x, y, [], [], [], screen2, 1
        self.turtle = turtle.Turtle()
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.turtle.up()
        for _ in range(12):
            self.p.append([x, y])
            self.dir.append(random.uniform(0, math.pi * 2))
            self.s.append(random.uniform(300, 500))

    def draw(self):
        self.turtle.clear()
        if self.t > 0:
            for i in range(len(self.p)):
                self.turtle.goto(self.p[i])
                self.turtle.dot(2)

    def move(self, t):
        self.t -= t
        for i in range(len(self.p)):
            self.p[i][0] += self.s[i] * t * math.cos(self.dir[i])
            self.p[i][1] += self.s[i] * t * math.sin(self.dir[i])
            self.s[i] *= 0.9

    def explode(self):
        self.move(1/20)
        self.draw()
        if self.t > 0:
            self.screen.ontimer(self.explode, 50)
        if s1.lives==0:
            self.screen.ontimer(self.turtle.clear, 1000)  # Clean up explosion if game ended

class Spaceship:
    maxspeed = 100

    def __init__(self, x, y, direction):
        self.x, self.y, self.thrustlife, self.speedx, self.speedy, self.direction = x, y, 0, 25, 40, direction
        self.turtle, self.alive, self.lives, self.tipx, self.tipy = turtle.Turtle(), False, 3, 0, 0
        self.turtle.showturtle()
        self.turtle.penup()
        self.turtle.color("white")

    def reset_position(self):
        self.x = 0
        self.y = 0
        self.direction = 0
        self.speedx = 0
        self.speedy = 0
        self.turtle.clear()
        self.turtle.showturtle()  # Show the ship when respawning
        self.alive = True
        self.thrustlife = 0
    
    def draw_one(self,x,y):
        dir_degree = self.direction * 180 / math.pi
        self.turtle.seth(dir_degree+90)
        self.turtle.setposition(self.x,self.y)

    def draw(self):
        self.turtle.clear()
        if self.alive or __name__ == '__main__':
            if self.x > 300:
                self.x -= 600
            if self.x < -300:
                self.x += 600
            if self.y > 300:
                self.y -= 600
            if self.y < -300:
                self.y += 600
            self.draw_one(self.x + 600, self.y)
            self.draw_one(self.x - 600, self.y)
            self.draw_one(self.x, self.y + 600)
            self.draw_one(self.x, self.y - 600)
            self.draw_one(self.x, self.y)

    def move(self, t):
        self.x, self.y, self.thrustlife = self.x + self.speedx * t, self.y + self.speedy * t, self.thrustlife - t

def spaceship_collision():
    if s1.alive:
        ship_radius = 15  # Approximate radius of the ship
        
        # Check collision for the actual ship position and its wrapped positions
        positions_to_check = [
            (s1.x, s1.y),
            (s1.x + 600, s1.y),
            (s1.x - 600, s1.y),
            (s1.x, s1.y + 600),
            (s1.x, s1.y - 600)
        ]
        
        for asteroid in asteroids:
            # Calculate approximate radius of asteroid (use average of random sizes)
            asteroid_radius = sum(asteroid.s) / len(asteroid.s)
            
            # Check each possible ship position against the asteroid
            for pos in positions_to_check:
                # Calculate distance between ship position and asteroid
                dx = pos[0] - asteroid.x
                dy = pos[1] - asteroid.y
                distance = math.sqrt(dx * dx + dy * dy)
                
                # If distance is less than combined radii, we have a collision
                if distance < (ship_radius + asteroid_radius):
                    # Create ship explosion before setting alive to false
                    ship_exp = Explosion(s1.x, s1.y, screen)
                    ship_exp.explode()
                    
                    s1.alive = False
                    s1.lives -= 1
                    s1.turtle.hideturtle()  # Hide the ship immediately
                    
                    # Handle asteroid splitting
                    if asteroid.size > 20:
                        for _ in range(2):
                            new_asteroid = Asteroid(
                                asteroid.size / 2,
                                asteroid.x,
                                asteroid.y,
                                asteroid.speed + 15
                            )
                            asteroids.append(new_asteroid)
                    
                    # Create asteroid explosion
                    asteroid_exp = Explosion(asteroid.x, asteroid.y, screen)
                    asteroid_exp.explode()
                    
                    # Remove the asteroid
                    asteroid.turtle.clear()
                    asteroids.remove(asteroid)
                    
                    if s1.lives > 0:
                        screen.ontimer(alive,2000)
                    else:
                        screen.ontimer(end_screen,2000)
                    return  # Exit after handling collision

def collision_detection():
    global score
    
    dead_asteroids = []
    dead_bullets = []
    
    if not asteroids:
        turtle.write('You Win', font=style, align='center')
        return
        
    # Check each bullet against each asteroid
    for bullet in bullets:
        for asteroid in asteroids:
            if asteroid not in dead_asteroids:
                # Calculate distance between bullet and asteroid center
                dx = bullet.x - asteroid.x
                dy = bullet.y - asteroid.y
                distance = math.sqrt(dx * dx + dy * dy)
                
                # Use average asteroid size for collision radius
                asteroid_radius = sum(asteroid.s) / len(asteroid.s)
                
                # If bullet is within asteroid radius, we have a hit
                if distance < asteroid_radius:
                    dead_asteroids.append(asteroid)
                    dead_bullets.append(bullet)
                    break
    
    # Handle dead asteroids
    for asteroid in dead_asteroids:
        if asteroid.size > 20:
            # Split into 3 smaller asteroids
            for _ in range(2):
                new_asteroid = Asteroid(
                    asteroid.size / 2,
                    asteroid.x,
                    asteroid.y,
                    asteroid.speed + 15
                )
                asteroids.append(new_asteroid)
            
            # Create explosion effect
            exp = Explosion(asteroid.x, asteroid.y, screen)
            exp.explode()
            score+=1
        else:
            # Small asteroids just explode
            exp = Explosion(asteroid.x, asteroid.y, screen)
            exp.explode()
            score+=2
        # Remove the destroyed asteroid
        asteroid.turtle.clear()
        asteroids.remove(asteroid)
    
    # Clean up dead bullets
    for bullet in dead_bullets:
        bullet.turtle.clear()
        bullets.remove(bullet)

def random_of_ranges(a,b):
    r1 = list(range(a[0],a[1]))
    r2 = list(range(b[0],b[1]))
    all_ranges = sum((r1,r2), [])
    return random.choice(all_ranges)

def animate():
    global asteroids, bullets
    if s1.alive:
        s1.move(1 / 20)
        s1.draw()
        for a in asteroids:
            a.move(frame)
            a.draw_two()
        for b in bullets:
            b.move(frame)
            b.draw()
        spaceship_collision()
        collision_detection()
        if len(bullets) > 0 and bullets[0].life < 0:
            bullets[0].turtle.clear()
            bullets.pop(0)
    else:
        alive()
    screen.update()
    screen.ontimer(animate, 50)

def visual_animate():
    global asteroids  # Add global declaration
    for a in asteroids:
        a.move(frame)
        a.draw_two()
    if animating:
        screen.ontimer(visual_animate, 50)
    screen.update()

def rotate_left():
    s1.direction += 0.2

def rotate_right():
    s1.direction -= 0.2

def thrust():
    if s1.alive:
        s1.thrustlife = 0.5
        thrust_direction = s1.direction + math.pi/2
        s1.speedx, s1.speedy = s1.speedx + 5 * math.cos(thrust_direction), s1.speedy + 5 * math.sin(thrust_direction)
        speed = (s1.speedx ** 2 + s1.speedy ** 2) ** 0.5
        if speed > Spaceship.maxspeed:
            s1.speedx, s1.speedy = (s1.speedx * Spaceship.maxspeed) / speed, (s1.speedy * Spaceship.maxspeed)/speed

def fire():
    if s1.alive:
        # Only allow 4 bullets at a time and enforce cooldown
        if len(bullets) < 4 and (len(bullets) == 0 or bullets[-1].life <= 2.0):
            # Add ship's velocity to bullet's velocity for realistic physics
            bullet_direction = s1.direction + math.pi/2
            b = Bullet(s1.x, s1.y, bullet_direction)
            
            # Add ship's velocity to bullet's initial velocity
            b.x += s1.speedx * frame  # Add ship's momentum
            b.y += s1.speedy * frame
            
            bullets.append(b)

def alive():
    if not s1.alive and s1.lives > 0:
        s1.reset_position()
        
        # Create a safe zone around the respawn point
        safe_zone_radius = 150
        
        # Move any asteroids that are too close to the spawn point
        for asteroid in asteroids:
            distance = math.sqrt(asteroid.x**2 + asteroid.y**2)  # Distance from center
            if distance < safe_zone_radius:
                # Calculate new position outside safe zone
                angle = random.uniform(0, 2 * math.pi)
                asteroid.x = safe_zone_radius * math.cos(angle)
                asteroid.y = safe_zone_radius * math.sin(angle)

def start_screen():
    start.ht()
    start.penup()
    start.goto(0,100)
    start.color("white")
    start.write("Asteroids",font=title,align="center")
    start.goto(0,-50)
    start.write("Click to start.",font=style,align="center")
    
    for i in range(10):
        a1 = Asteroid(random.randint(15,50),random.randint(-200,200),random.randint(-200,200),random.randint(20,40))
        a1.draw_one(0,0)
        asteroids.append(a1)
    visual_animate()
    
    screen.onclick(start_game)

def start_game(x,y):
    global animating, start, asteroids, bullets  # Add asteroids and bullets to global
    screen.onclick(None)
    start.clear()
    animating = False
    
    screen.onkeypress(rotate_left, 'a')
    screen.onkeypress(rotate_right, 'd')
    screen.onkeypress(thrust, 'w')
    screen.onkeypress(fire, 'space')
    
    for i in asteroids:
        # Clear existing asteroids
        i.turtle.clear()
    for i in range(5):
        a1 = Asteroid(random.randint(15,50),
                    random_of_ranges([-300,-100],[100,300]),
                    random_of_ranges([-300,-100],[100,300]),
                    random.randint(20,40))
        asteroids.append(a1)
    
    alive()
    screen.listen()
    animate()

def end_screen():
    global animating
    animating = False
    
    # Clear all existing objects immediately
    for asteroid in asteroids[:]:  # Create a copy of the list to iterate over
        asteroid.turtle.clear()
    asteroids.clear()
    
    for bullet in bullets[:]:  # Create a copy of the list to iterate over
        bullet.turtle.clear()
    bullets.clear()
    
    s1.turtle.clear()
    
    screen.clear()
    turtle.bgcolor(0,0,0)
    
    # Create end screen
    end = turtle.Turtle()
    end.ht()
    end.penup()
    end.goto(0,100)
    end.color("white")
    end.write("You died.",font=title,align="center")
    end.goto(0,0)
    end.write("Better luck next time?",font=style,align="center")
    end.goto(0,-200)
    end.write("Score: "+str(score),font=style,align="center")

# Initialize game variables
turtle.bgcolor(0,0,0)
title = ('Courier', 40, 'normal')
style = ('Courier', 15, 'normal')

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0, 0)
frame = 1/20

start = turtle.Turtle()
animating = True

s1 = Spaceship(0, 0, 0)
bullets = []
asteroids = []
score = 0

start_screen()

turtle.mainloop()