
# Friction, Gravity, and Player Controlled Acceleration

Location and velocity-based movement covers a lot of bases in our movement design matrix, but leaves a couple of very glaring hole: jumping and running. If we want our player to jump, then
we not only need to add upward velocity, but we need gravity to work against that velocity and eventually change its direction. Similarly, running means starting out slow, building up speed, then decelerating smoothly once the player has stopped pressing the movement key. What we're talking about is given players a variable velocity rather than a constant velocity assigned at the moment of pressing a key. Put another way, players should accelerate their character when they press a movement key. Acceleration then increases velocity, which in turn changes position. This also makes room for decelerating forces: friction on the ground and gravity in the air.

# Designing for Running and Jumping

Let's stop for a minute and think about what a natural feeling running and jumping experience might entail.  First, running.  When on the ground, pressing the left or right movement key should start the player moving in the desired direction. Initial movement is slow, but the longer they hold down the key, the faster they'll move up to some max velocity. When the key is released, the character should decelerate and stop moving. 
