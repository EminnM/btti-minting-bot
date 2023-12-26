# btti-minting-bot
btti mint'lemek için bir python bot'u.

## Özel Anahtarınızı Edinin

Metamask ya da başka bir cüzdandan "Private Key" gizli anahtarınızı edinin. Gizli anahtarınızı kod çalışırken terminale yapıştırmanız gerekecek.

## Kurulum

### Windows Kullanıcıları İçin
Eğer bilgisayarınızda Python yüklü değilse, aşağıdaki adımları takip edin:

1. Python'un Windows'ta nasıl kurulacağını gösteren bu [video kılavuzunu](https://www.youtube.com/watch?v=ERcsRnUQ64s) izleyin.

2. Alternatif olarak, aşağıdaki yazılı talimatları takip edebilirsiniz:

   - Web tarayıcınızı açın ve [resmi Python web sitesine](https://www.python.org/) gidin.
   - "Downloads" (İndirmeler) bölümüne gidin.
   - "Latest Python 3 Release" (En Son Python 3 Sürümü) bağlantısına tıklayın.
   - Sayfanın aşağısına inin ve sistem tipinize bağlı olarak (32-bit veya 64-bit) "Windows x86-64" için 64-bit veya "Windows x86" için 32-bit olan yükleyiciyi seçin.
   - Yükleyiciyi çalıştırın ve yükleme sırasında "Add Python to PATH" (Python'u PATH'e ekle) seçeneğini işaretleyin. Burası kritik. Bunu yapmazsanız çalışmaz
   - ![Resim](https://github.com/EminnM/XRPS-minting-bot/assets/63583116/48e43f9a-218d-4995-9bf6-db221df52a32)
   - "Install Now" (Şimdi Yükle) düğmesine tıklayın ve ekrandaki talimatları izleyin.
   - Python'ı yükledikten sonra terminali açın ve yüklemeyi doğrulamak için aşağıdaki komutu yazın:
     ```bash
     python --version
     ```

     Yüklü Python sürümünü görüyorsanız kurulum tamamdır. Ardından şu komutları teker teker yazıp enter'a basın:

     ```bash
     pip install web3
     pip install pwinput

     ```

  
     Sonrasında [GitHub](https://github.com/EminnM/btti-minting-bot/) sayfasına gidin.
     Sağ üstteki yeşil "Code" düğmesine tıklayın.
     "Download ZIP" seçeneğini seçin.
     ZIP dosyasını istediğiniz yere ayıklayın.
     Cmd'yi açın ve çıkarılan klasöre gitmek için şu komutu yazın:
     ```bash
     cd path/to/btti-minting-bot
     minting-bot.py
     ```

     burdaki path/to kısmı bir değişken olup
     Diyelim ki dosyayı indirilenler klasörüne ayıkladınız o zaman örneğin
     Cd downloads
     Cd btti-minting-bot
     şeklinde minting-bot.py dosyasının olduğu konuma gidebilirsiniz 
      

### MacOs Kullanıcıları İçin
Eğer bilgisayarınızda Python yüklü değilse, aşağıdaki adımları takip edin:

1. Python'un Mac'te nasıl kurulacağını gösteren bu [video kılavuzunu](https://www.youtube.com/watch?v=5zX1MkAHdKU) izleyin.

2. Veya web tarayıcınızı açın ve [resmi Python web sitesine](https://www.python.org/) gidin.

   - "Downloads" (İndirmeler) bölümüne gidin.
   - "Latest Python 3 Release" (En Son Python 3 Sürümü) bağlantısına tıklayın.
   - Sayfanın aşağısına inin ve macOS yükleyicilerini göreceksiniz. Sisteminize uygun olanı seçin.
   - Yükleyiciye tıklayın ve ekrandaki talimatları izleyin.
   - Python'ı yükledikten sonra terminali açın ve yüklemeyi doğrulamak için şu komutu yazın:
     ```bash
     python --version
     ```

     Yüklü Python sürümünü görüyorsanız kurulum tamamdır. Ardından şu komutları teker teker yazıp enter'a basın:

     ```bash
     pip install web3
     pip install pwinput

     ```


     [GitHub](https://github.com/EminnM/btti-minting-bot/) deposuna gidin.
     Yeşil "Code" düğmesine tıklayın.
     "Download ZIP" seçeneğini seçin.
     ZIP dosyasını istediğiniz yere çıkarın.
     Terminali açın ve çıkarılan klasöre gitmek için şu komutu yazın:
     ```bash
     cd path/to/btti-minting-bot
     ```
     burdaki path/to kısmı bir değişken olup
     Diyelim ki dosyayı indirilenler klasörüne ayıkladınız o zaman örneğin
     Cd downloads
     Cd btti-minting-bot
     şeklinde minting-bot.py dosyasının olduğu konuma gidebilirsiniz 
     Botu çalıştırmak için
     ```bash
     python3 minting-bot.py
     ```

