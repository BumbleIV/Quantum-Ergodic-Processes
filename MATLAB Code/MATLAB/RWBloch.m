lambda=.4;
delta = pi;
N=2000;
v0 = [1 0 0]';
theta = pi/3;
omega = 1;
phi = 0;
p=.4;
%marr = 50;


v = zeros(3,N+1);
v(:,1)=v0;

for j=1:N
    u = [sin(theta)*cos(phi), sin(theta)*sin(phi),cos(theta)]';
    phi = phi +omega*(randi([0,1])-1);
    v(:,j+1) = lambda * u + (1-lambda)*dot(u,v(:,j))*u... 
        +sqrt(1-lambda)*(cos(delta)*(v(:,j)- dot(u,v(:,j))*u)...
            + sin(delta)*cross(v(:,j),u));
end

figure;
[x y z] = sphere;
ax1 = axes;
h = surfl(ax1,x,y,z);
set(h,'EdgeAlpha',0.1,'FaceAlpha',.1);
colormap(ax1,summer);
axis equal;
ax2 = axes;
norm = vecnorm(v,2,1);
%colors = 0.75*[(1-norm(:)).^p (1-norm(:)).^p (1-norm(:)).^p];
%colors = [0.75+0.25*norm(:).^p.*(1-norm(:)).^p  0.75*(1-norm(:)).^p 0.75*(1-norm(:)).^p];
colors = [0.3*(1-norm(:)).^p 0.6*(1-norm(:)).^p 0.9*(1-norm(:)).^p];
%colors = [0.1+0.9*norm(:).^p.*(1-norm(:)).^p  0.1 + 0.9*norm(:).^p.*(1-norm(:)).^p (1-norm(:)).^p];
%colors = [zeros(size(norm(:))) (1-norm(:)).^p  0.5 + 0.5*norm(:).^p];
%colors = [zeros(size(norm(:))) norm(:).^p 0.5 + 0.5*(1-norm(:)).^p ];
%colors = [(norm(:)).^p 0*(1-(norm(:)).^p) (1-(norm(:)).^p)];
scatter3(ax2,v(1,:),v(2,:),v(3,:),20,colors,'filled');
hold on;
scatter3(ax2,v(1,1),v(2,1),v(3,1),20,'r+');
patch(ax2,[v(1,:) nan] ,[v(2,:) nan],[v(3,:) nan],1:(N+2),'EdgeColor','interp','FaceColor','none');
colormap(ax2,colors);
axis equal;
hLink = linkprop([ax1,ax2],{'XLim','YLim','ZLim','CameraUpVector','CameraPosition','CameraTarget'});
ax1.Visible = 'off';
ax2.Visible = 'off';