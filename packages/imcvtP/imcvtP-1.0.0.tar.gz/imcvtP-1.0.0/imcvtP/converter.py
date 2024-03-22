import glob
from PIL import Image
# 에러가 안나게 견고하게 설계해야 개발 실력이 많이 향상됨.
class GifConverter :
    def __init__ (self, path_in=None, path_out=None, resize = (320,240)):
        """
        path_in : 원본 여러 이미지 경로(Ex : images/*.png)
        path_ou : 결과 이미지 경로(Ex : output/filename.gif)
        resize : 리사이징 크기 ((320,240))
        """
        self.path_in = path_in or './*.png' # 같은 경로에 png를 쓰거나 아니면 해당경로에자동으로 png 파일 찾기
        self.path_out = path_out or './output.gif'
        self.resize = resize
        
    def convert_gif(self) :
        """
        GIF 이미지 변환 기능 수행
        """
        print(self.path_in, self.path_out, self.resize) # 배포할떄는 print가아니라 logging을 이용해서 만들어야함
        
        img, *images = \
            [Image.open(f).resize(self.resize,Image.ANTIALIAS) for f in sorted(glob.glob(self.path_in))]
            
        try :
            img.save(
                        fp = self.path_out,
                        format = 'GIF',
                        append_images = images,
                        save_all = True,
                        duration = 500,
                        loop = 0
                    )
        except IOError :
            print('Cannot convet!', img)


if __name__ == '__main__' :
    path_in = './project/images/*.png'
    path_out = './project/image_out/result.gif'
    c = GifConverter(path_in, path_out,(320,240))
    c.convert_gif()
