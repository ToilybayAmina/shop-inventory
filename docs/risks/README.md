# Risks — Shop-Inventory

## Файлдар

| Файл | Сипаттама |
|---|---|
| [pre-mortem.md](pre-mortem.md) | 22 тәуекел |
| [raid-journal.md](raid-journal.md) | 32 жол RAID-журнал |
| [stride-model.md](stride-model.md) | 12 STRIDE қауіп |
| [compliance-checklist.md](compliance-checklist.md) | Сәйкестік чек-лист |
| [stride-model.png](stride-model.png) | STRIDE диаграмма |

## Негізгі нәтижелер

- **22 тәуекел** (pre-mortem)
- **12 STRIDE қауіп** (аутентификация + деректер алмасу)
- **5 топ тәуекел** толық жазылған
- **3 тәуекелді азайту шарасы** бэклогқа енгізілді
- **CI-де Trivy + gitleaks** автоматты қауіпсіздік

## Тәуекелдерді басқару

| Тәуекел | Бағасы | Иесі |
|---|---|---|
| R-01: Мерзім | 🔴 | PM |
| R-05: Тестілеу | 🔴 | QA |
| R-11: Жеке деректер | 🔴 | PM |
| R-17: Құпия сөздер | 🔴 | PM |
| R-22: Жоба қайта | 🔴 | PM |
