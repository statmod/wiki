---
title: "ImageMagick: Скриншоты"
---

 Снятие скриншота с помощью [ImageMagick](imagick.md) тривиально.


## Windows


1.  Нажмите PrintScreen (или Alt+PrintScreen на клавиатуре). Это действие поместит изображение всего экрана (или текущего окна) в буфер обмена.
2.  Вызовите:
        convert.exe clipboard:myimage myimage.png
3.  В текущем каталоге появится файл myimage.png


## Linux

 Достаточно вызвать <code> import -window root screen.ps </code>

**Замечание**: [ImageMagick](imagick.md) определяет формат вывода по расширению. Для того, чтобы получить файл в формате JPEG достаточно вместо `myimage.png` указать `myimage.jpg`. Аналогично, для получения изображения в формате EPS - `myimage.eps`