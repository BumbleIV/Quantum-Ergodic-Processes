# Generated with SMOP  0.41
from libsmop import *
# Bloch copy.m

lambda_ = 0.01
# Bloch copy.m:1
delta = pi / 12
# Bloch copy.m:2
N = 3000
# Bloch copy.m:3
v0 = concat([1, 0, 0]).T
# Bloch copy.m:4
theta = pi / 2
# Bloch copy.m:5
omega = 1.1
# Bloch copy.m:6
p = 0.4
# Bloch copy.m:7
marr = 8
# Bloch copy.m:8
phi = 0
# Bloch copy.m:10
v = zeros(3, N + 1)
# Bloch copy.m:11
v[arange(), 1] = v0
# Bloch copy.m:12
for j in arange(1, N).reshape(-1):
    u = concat([dot(sin(theta), cos(phi)), dot(
        sin(theta), sin(phi)), cos(theta)]).T
# Bloch copy.m:15
    phi = phi + omega
# Bloch copy.m:16
    v[arange(), j + 1] = dot(lambda_, u) + dot(dot((1 - lambda_), dot(u, v(arange(), j))), u) + dot(sqrt(1 - lambda_),
                                                                                                    (dot(cos(delta), (v(arange(), j) - dot(dot(u, v(arange(), j)), u))) + dot(sin(delta), cross(v(arange(), j), u))))
# Bloch copy.m:17

    figure
    x, y, z = sphere
# Bloch copy.m:23
    ax1 = copy(axes)
# Bloch copy.m:24
    h = surfl(ax1, x, y, z)
# Bloch copy.m:25
    set(h, 'EdgeAlpha', 0.1, 'FaceAlpha', 0.1)
    colormap(ax1, summer)
    axis('equal')
    ax2 = copy(axes)
# Bloch copy.m:29
    norm = vecnorm(v, 2, 1)
# Bloch copy.m:30
    # colors = 0.75*[(1-norm(:)).^p (1-norm(:)).^p (1-norm(:)).^p];
# colors = [0.75+0.25*norm(:).^p.*(1-norm(:)).^p  0.75*(1-norm(:)).^p 0.75*(1-norm(:)).^p];
    colors = concat([dot(0.3, (1 - ravel(norm)) ** p), dot(0.6,
                    (1 - ravel(norm)) ** p), dot(0.9, (1 - ravel(norm)) ** p)])
# Bloch copy.m:33
    # colors = [0.1+0.9*norm(:).^p.*(1-norm(:)).^p  0.1 + 0.9*norm(:).^p.*(1-norm(:)).^p (1-norm(:)).^p];
# colors = [zeros(size(norm(:))) (1-norm(:)).^p  0.5 + 0.5*norm(:).^p];
# colors = [zeros(size(norm(:))) norm(:).^p 0.5 + 0.5*(1-norm(:)).^p ];
# colors = [(norm(:)).^p 0*(1-(norm(:)).^p) (1-(norm(:)).^p)];
    scatter3(ax2, v(1, arange()), v(2, arange()),
             v(3, arange()), 20, colors, 'filled')
    hold('on')
    scatter3(ax2, v(1, 1), v(2, 1), v(3, 1), 20, 'r+')
    patch(ax2, concat([v(1, arange()), nan]), concat([v(2, arange()), nan]), concat(
        [v(3, arange()), nan]), arange(1, (N + 2)), 'EdgeColor', 'interp', 'FaceColor', 'none')
    colormap(ax2, colors)
    axis('equal')
    hLink = linkprop(concat([ax1, ax2]), cellarray(
        ['XLim', 'YLim', 'ZLim', 'CameraUpVector', 'CameraPosition', 'CameraTarget']))
# Bloch copy.m:44
    ax1.Visible = copy('off')
# Bloch copy.m:45
    ax2.Visible = copy('off')
# Bloch copy.m:46
