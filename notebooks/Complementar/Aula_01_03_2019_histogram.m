clc
close all
clear all

%%

img = imread('lena_color_512.tif');
img_gray = rgb2gray(img);

%% Histogram: gráfico de frequência. Distribuição de probabilidade.

idx = zeros(1,256);
[lin, col] = size(img_gray);

valor_min = double(min(min(img_gray)))
valor_max = double(max(max(img_gray)))

for k=1:lin
   for l=1:col 
       idx(img_gray(k,l)) = idx(img_gray(k,l)) + 1;
       
       % Equalização
       x = double(img_gray(k,l));
       y(k,l) = double(((valor_max - valor_min) * ((x - 255)/255)) + valor_max);
   end
end

%% Histogram

idx_y = zeros(1,256);
[lin, col] = size(img_gray);

img_y = uint8(y);
limiar = 150

for k=1:lin
   for l=1:col 
       idx_y(img_y(k,l)) = idx_y(img_y(k,l)) + 1;
       
       % Limirização
       
   end
end

%%
figure; 
imshow(img_gray)

figure;
imshow(uint8(y))


%%
figure
plot(idx)

figure
plot(idx_y)























































