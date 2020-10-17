clc
close all
clear all

%%

img = imread('lena_color_512.tif');
img_gray = rgb2gray(img);

%% Media
tamanho = 11;

kernel = zeros(tamanho);
kernel(:,:) = 1/(tamanho^2);

%% Padding
offset = floor(tamanho/2)
[lin, col] = size(img_gray)

img_buffer = zeros(lin+2*offset, col+2*offset);
img_buffer(1+offset:lin+offset, 1+offset:col+offset) = img_gray;


%% Convoluçao

for k = 1+offset:lin+1
   for  l = 1+offset:col+1
       resultado = kernel .* double(img_buffer(k-offset:k+offset,l-offset:l+offset));
       resultado = sum(sum(resultado));
       img_buffer(k,l) = resultado;
   end
end

img_out = uint8(img_buffer)
%% Plotar image

imshow(img_out)










