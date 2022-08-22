#version 400

layout (location=0) in vec3 position;
layout (location=1) in vec3 normal;
uniform mat4 MVP;

varying float intensity;

void main(void)
{
	vec3 lightDir = normalize(vec3(10.0,0.0,10.0));
	intensity = dot(lightDir,normal);

    gl_Position = MVP * vec4(position,1.0);
}
