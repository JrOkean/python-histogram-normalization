# Equalização Histogramica de Um Vídeo Baseado em Uma Avaliação Por Desvio Padrão

Passos:
1. Carrega-se um vídeo de um repositório embutido;
2. Segui-se para a chamada da função `ret, frame = cap.read()`, que é do OpenCV, carregando o vídeo quadro a quadro ([Playing Video from file](https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html));
3. Tranforma-se, então, esse frame em uma `gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)` imagem em escala cinza;
4. Usa-se a função `yeah, h_ = avalia_pic(gray)`, que calcula o `np.histogram` e alguns valores associados, como `desvio_, media_` e `coff`, que refere-se ao coeficiente de variação da distribuição de frequência, usando a bibliota Numpy;
   - Para receber os valores de desvio e média é usada a função `_desvio_padrao`, que calcula a média e o desvio padrão e os retorna.
5. Usando esse coeficiente de variação, espera-se inferir se os dados estão dipersos com relação a média ou não, e, se não estiverem, então a imagem será equalizada, portanto retornamos um `bool` — que representa esse sim ou não;
6. 