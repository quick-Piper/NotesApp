document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('bd-theme');
    const themeIcons = {
        light: document.querySelector('use[href="#sun-fill"]'),
        dark: document.querySelector('use[href="#moon-stars-fill"]'),
        auto: document.querySelector('use[href="#circle-half"]')
    };

    const currentTheme = localStorage.getItem('theme') || 'auto';
    document.body.setAttribute('data-bs-theme', currentTheme);

    function updateTheme(newTheme) {
        document.body.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        for (const [theme, icon] of Object.entries(themeIcons)) {
            icon.classList.toggle('d-none', theme !== newTheme);
        }
    }

    themeToggle.addEventListener('click', function () {
        const currentTheme = document.body.getAttribute('data-bs-theme');
        let newTheme;

        if (currentTheme === 'auto') {
            newTheme = 'light';
        } else if (currentTheme === 'light') {
            newTheme = 'dark';
        } else {
            newTheme = 'auto';
        }
 
        updateTheme(newTheme);
    });

    updateTheme(currentTheme);
});
