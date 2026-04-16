// БАЗА ДАННЫХ УГОЛОВНЫХ ДЕЛ (тестовые данные)
const criminalCases = [
    {
        caseNumber: "1-22/2024",
        defendant: "Сидоров Петр Алексеевич",
        victim: "ООО 'Ромашка'",
        article: "ст. 159 УК РФ (мошенничество)",
        status: "В суде",
        judge: "Иванова А.А.",
        date: "15.03.2024"
    },
    {
        caseNumber: "1-45/2024",
        defendant: "Козлова Мария Ивановна",
        victim: "Петрова Е.С.",
        article: "ст. 158 УК РФ (кража)",
        status: "Приговор вынесен",
        judge: "Смирнов В.В.",
        date: "10.02.2024"
    },
    {
        caseNumber: "1-78/2024",
        defendant: "Волков Дмитрий Сергеевич",
        victim: "ИП 'Успех'",
        article: "ст. 160 УК РФ (присвоение)",
        status: "Расследуется",
        judge: "Нет",
        date: "01.04.2024"
    },
    {
        caseNumber: "1-12/2024",
        defendant: "Новикова Анна Владимировна",
        victim: "Сбербанк",
        article: "ст. 159.3 УК РФ (мошенничество с использованием электронных средств)",
        status: "Назначено заседание",
        judge: "Морозова Е.А.",
        date: "20.01.2024"
    },
    {
        caseNumber: "1-99/2023",
        defendant: "Морозов Иван Петрович",
        victim: "Гражданин Петров П.П.",
        article: "ст. 111 УК РФ (причинение тяжкого вреда здоровью)",
        status: "Отбывает наказание",
        judge: "Лебедев А.А.",
        date: "10.12.2023"
    },
    {
        caseNumber: "1-33/2024",
        defendant: "Соколова Екатерина Дмитриевна",
        victim: "Магазин 'Электроника'",
        article: "ст. 161 УК РФ (грабёж)",
        status: "В суде",
        judge: "Иванова А.А.",
        date: "05.03.2024"
    }
];
// Функция поиска по номеру дела и ФИО
function searchCases(caseNumber, fullName) {
    // Если оба поля пустые
    if (!caseNumber && !fullName) {
        return { error: "Введите номер дела или ФИО для поиска" };
    }
    
    let results = [];
    
    // Поиск по каждому делу
    for (let i = 0; i < criminalCases.length; i++) {
        const caseItem = criminalCases[i];
        let match = false;
        
        // Поиск по номеру дела (частичное совпадение)
        if (caseNumber && caseItem.caseNumber.toLowerCase().includes(caseNumber.toLowerCase())) {
            match = true;
        }
        
        // Поиск по ФИО (частичное совпадение)
        if (fullName && caseItem.defendant.toLowerCase().includes(fullName.toLowerCase())) {
            match = true;
        }
        
        if (match) {
            results.push(caseItem);
        }
    }
    
    // Если ничего не найдено
    if (results.length === 0) {
        return { error: "По вашему запросу ничего не найдено. Проверьте введённые данные." };
    }
    
    return results;
}
// Функция отображения результатов
function displayResults(results) {
    const container = document.getElementById('searchResults');
    
    if (!container) return;
    
    // Очищаем предыдущие результаты
    container.innerHTML = '';
    
    // Если ошибка
    if (results.error) {
        container.innerHTML = `<div class="error-message">⚠️ ${results.error}</div>`;
        return;
    }
    
    // Отображаем каждое найденное дело
    for (let i = 0; i < results.length; i++) {
        const caseItem = results[i];
        const resultCard = document.createElement('div');
        resultCard.className = 'result-card';
        resultCard.innerHTML = `
            <h3>📁 Дело № ${caseItem.caseNumber}</h3>
            <div class="result-details">
                <div><strong>Обвиняемый:</strong> ${caseItem.defendant}</div>
                <div><strong>Потерпевший:</strong> ${caseItem.victim}</div>
                <div><strong>Статья:</strong> ${caseItem.article}</div>
                <div><strong>Статус:</strong> ${caseItem.status}</div>
                <div><strong>Судья:</strong> ${caseItem.judge}</div>
                <div><strong>Дата возбуждения:</strong> ${caseItem.date}</div>
            </div>
        `;
        container.appendChild(resultCard);
    }
}
// Обработчик кнопки "Найти"
function performSearch() {
    const caseNumberInput = document.getElementById('caseNumber');
    const fullNameInput = document.getElementById('fullName');
    
    const caseNumber = caseNumberInput ? caseNumberInput.value.trim() : '';
    const fullName = fullNameInput ? fullNameInput.value.trim() : '';
    
    const results = searchCases(caseNumber, fullName);
    displayResults(results);
}
// Обработчик кнопки "Очистить"
function resetSearch() {
    const caseNumberInput = document.getElementById('caseNumber');
    const fullNameInput = document.getElementById('fullName');
    const resultsContainer = document.getElementById('searchResults');
    
    if (caseNumberInput) caseNumberInput.value = '';
    if (fullNameInput) fullNameInput.value = '';
    
    if (resultsContainer) {
        resultsContainer.innerHTML = '<div class="no-results">🔍 Введите номер дела или ФИО для поиска</div>';
    }
}
// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    const searchBtn = document.getElementById('searchBtn');
    const resetBtn = document.getElementById('resetBtn');
    
    if (searchBtn) {
        searchBtn.addEventListener('click', performSearch);
    }
    
    if (resetBtn) {
        resetBtn.addEventListener('click', resetSearch);
    }
    
    console.log("✅ Поиск уголовных дел загружен. Доступно дел: " + criminalCases.length);
});