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

// 모달 바깥 클릭시 닫기
document.getElementById('loginModal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeLogin();
    }
});

// 로그인 (나중에 백엔드 연결)
function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password) {
        alert('아이디와 비밀번호를 입력해주세요');
        return;
    }

    // 나중에 여기에 API 연결
    // fetch('/api/login', { ... })
    alert('로그인 기능은 백엔드 개발 후 연결될 예정입니다!');
}

// ESC 키로 모달 닫기
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeLogin();
    }
});
