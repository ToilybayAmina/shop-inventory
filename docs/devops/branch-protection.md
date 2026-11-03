# Негізгі тармақты қорғау ережелері

`main` тармағына тікелей өзгерістер енгізуге тыйым салынған. Барлық өзгерістер Pull Request (PR) арқылы ғана қабылданады.

## Бапталған ережелер (GitHub Settings → Branches):

1. **Require a pull request before merging:** Кез келген өзгеріс тек PR арқылы кіреді.
2. **Require approvals:** Кемінде 1 code review мақұлдауы болуы шарт.
3. **Require status checks to pass before merging:** CI пайплайн (lint, test, security_scan) сәтті өтпейінше, PR-ды біріктіруге болмайды.
4. **Require conversation resolution before merging:** Барлық пікірлер шешілуі керек.
