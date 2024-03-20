from src.SanauAutomationSDK.SanauAutomationSDK import SanauAutomationSDK
sasdk = SanauAutomationSDK('KZ', 'pbo.kz', '7nuLUYDYeQLyd3Rn')

print(sasdk.oked.get_all_okeds({'API-ACCESS-TOKEN': 'f6f9e9272531a31defdbb4ea778b3997'}))