extends KinematicBody2D

func _process(delta):
	if Input.is_action_pressed("ui_right"):
		$AnimatedSprite.play("run")
	else:
		$AnimatedSprite.stop()
