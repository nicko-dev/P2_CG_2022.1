#version 400

out vec4 color;

varying float intensity;

void main(void)
{
	if (intensity > 0.95)
		color = vec4(0.5,1.0,0.5,1.0);
	else if (intensity > 0.65)
		color = vec4(0.3,0.6,0.3,1.0);
	else if (intensity > 0.425)
		color = vec4(0.2,0.4,0.2,1.0);
    else if (intensity > 0.25)
		color = vec4(0.1,0.2,0.1,1.0);
    else if (intensity > 0.15)
		color = vec4(0.0,0.15,0.09,1.0);
	else
		color = vec4(0.05,0.1,0.05,1.0);
	//color = vec4(intensity, intensity, intensity, 1.0f);

}
