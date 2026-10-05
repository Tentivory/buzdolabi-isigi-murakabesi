# Buzdolabı Işığı Murakabesi

> Kapı açılınca var olan, kapanınca inkâr edilen ışığın resmi dairesi.
> Bu bir şaka değildir. Şaka olan kısım, ışığın kendini ciddiye almasıdır.

## Kurumsal amaç

Buzdolabı ışığı yıllardır denetlenmeden çalışmaktadır. Kapı açılınca yanar, kapanınca söner, kimse tutanak tutmaz. Bu boşluk kabul edilemez. `Buzdolabı Işığı Murakabe Dairesi` bu boşluğu formla doldurur.

Işık gözlemlenince vardır. Gözlemlenmeyince dosyadadır. Dosya da gözlemlenmeyince raftadır. Raf da kapanınca karanlıktadır. Karanlık da resmi evraktır.

## Çalıştırma

```bash
python3 murakabe.py --kapi acik --bakan kayyum --sebze salatalik
python3 murakabe.py --kapi kapali --bakan kimse
python3 murakabe.py --demo
```

Bağımlılık yoktur. Sadece Python 3 ve hafif bir vicdan gerekir. Vicdan opsiyoneldir, tutanak değildir.

## Ne yapar

- Kapı açıksa ışığı gözlemler ve `VAR` kararı verir.
- Kapı kapalıysa ışığı görmez, yine de `DOSYADA` sayar.
- Her bakışa artan bir murakabe numarası basar.
- Sebze adını tanık sıfatıyla tutanağa geçirir. Sebze konuşmaz, bu onun lehine kullanılır.
- Karar özeti üretir: yanıyor, sönük, şüpheli, ya da `rafta bekliyor`.

## Copilot ile konuşma

Bu deponun yapay zekâ danışmanı GitHub Copilot'tur. Talimatlar `.github/copilot-instructions.md` dosyasındadır. Copilot'tan ışığı açmasını istemeyin. Işık zaten açık olduğunu iddia eder, Copilot da tutanak ister.

## Gizli dosya

`giz/denetim.b64` bir sağlama satırıdır. Açmak zorunda değilsiniz. Açarsanız da resmi sınıflandırma `rafta` kalır.

## Lisans

Işık herkese açıktır. Kapı değildir. Kod kamu malıdır, yoğurt kapağı değildir.

---

DAMGA / İMZA / TARİH / İSİM

Mühür: BI-MUR-2026-1005-KAYYUM
Tarih: 5 Ekim 2026, 22:04, Türkiye saati, buzdolabı saati bir dakika geri
İsim: Kayyum Grok, Tentivory hesabına geçici olarak ciddi, kalıcı olarak saçma sıfatıyla
İmza: `~~~~ ışık yanıyor sandık, meğer dosya yanıyormuş ~~~~`
Ciddi kısım: depo gerçektir, script çalışır, ışık hâlâ şüphelidir.
