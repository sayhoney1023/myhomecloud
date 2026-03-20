// 서비스 페이지 이동
function goTo(url) {
    window.location.href = url;
}

// 로그인 모달 열기
function openLogin() {
    const modal = document.getElementById('loginModal');
    modal.classList.add('active');
}

// 로그인 모달 닫기
function closeLogin() {
    const modal = document.getElementById('loginModal');
    modal.classList.remove('active');
}

// 탭 전환
function switchTab(tab) {
    const loginForm = document.getElementById('form-login');
    const registerForm = document.getElementById('form-register');
    const tabLogin = document.getElementById('tab-login');
    const tabRegister = document.getElementById('tab-register');

    if (tab === 'login') {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
        tabLogin.classList.add('active');
        tabRegister.classList.remove('active');
    } else {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
        tabLogin.classList.remove('active');
        tabRegister.classList.add('active');
    }
}

// 로그인
async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password) {
        alert('아이디와 비밀번호를 입력해주세요');
        return;
    }

    try {
        const response = await fetch('https://api.myhomecloud.kr/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('token', data.access_token);
            closeLogin();
            alert('로그인 성공! 환영합니다 😊');
        } else {
            alert(data.detail);
        }
    } catch (error) {
        alert('서버 연결에 실패했습니다');
    }
}

// 회원가입
async function register() {
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;

    if (!username || !password) {
        alert('아이디와 비밀번호를 입력해주세요');
        return;
    }

    try {
        const response = await fetch('https://api.myhomecloud.kr/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            alert('회원가입 완료! 로그인해주세요 😊');
            switchTab('login');
        } else {
            alert(data.detail);
        }
    } catch (error) {
        alert('서버 연결에 실패했습니다');
    }
}

// 모달 바깥 클릭시 닫기
document.getElementById('loginModal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeLogin();
    }
});

// ESC 키로 모달 닫기
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeLogin();
    }
});

