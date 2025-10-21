document.addEventListener("DOMContentLoaded", () => {
	const toggle_btn = document.querySelectorAll('.toggle-theme');
	toggle_btn.forEach((btn)=> {
		btn.addEventListener("click", () => {
			if (document.documentElement.classList.contains('dark'))
			{
				document.documentElement.classList.remove("dark");
				localStorage.setItem('theme', 'light');
			}
			else
			{
				document.documentElement.classList.add("dark");
				localStorage.setItem('theme', 'dark');
			}
		});
	});

	
	const delete_container = document.createElement("div");
	document.querySelector("main").appendChild(delete_container);
	delete_container.setAttribute("id", "delete-post-confirm");
	delete_container.style.display = 'none';
	
	const delete_btns = document.querySelectorAll(".delete_btn");
	delete_btns.forEach(btn => {
		btn.addEventListener("click", () => {
			if (delete_container.style.display == 'none')
			{
				const htmlstring = `
					<div class="container-delete bg-gray-200">
						<p class="text-base leading-relaxed text-gray-900 dark:text-gray-100">
							Are you sure you want to delete ${btn.getAttribute("value")} post
						</p>
						<div class="mt-4 flex items-center justify-end gap-3">
							<form action="" method="post" class="inline">
								<input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
								<input type="hidden" name="slug" value="${btn.getAttribute("data-slug")}">
								<button type="submit"
										class="btn px-4 py-2 bg-red-600 hover:bg-red-700 text-white 
										rounded-md font-medium focus:outline-none focus:ring-2 focus:ring-red-500">
								Yes
								</button>
							</form>

							<button id="no-btn"
									class="btn px-4 py-2 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600
									text-gray-800 dark:text-gray-100 rounded-md font-medium focus:outline-none focus:ring-2 
									focus:ring-cyan-500">
								No
							</button>
						</div>
					</div>
				`;
				delete_container.innerHTML = htmlstring;
				delete_container.style.display = "flex";
			}
		})
	});
	
	delete_container.addEventListener("click", (event) => {
		if (event.target.matches('#no-btn')) {
			delete_container.style.display = "none";
		}
	});

});

(function () {
const toggle = document.getElementById('nav-toggle');
const mobileNav = document.getElementById('mobile-nav');

if (!toggle || !mobileNav) return;

function setExpanded(expanded) {
	toggle.setAttribute('aria-expanded', String(expanded));
	if (expanded) {
	mobileNav.classList.remove('hidden');
	} else {
	mobileNav.classList.add('hidden');
	}
}

toggle.addEventListener('click', function (e) {
	const expanded = toggle.getAttribute('aria-expanded') === 'true';
	setExpanded(!expanded);
});

document.addEventListener('click', function (e) {
	if (!mobileNav.classList.contains('hidden')) {
	if (!mobileNav.contains(e.target) && !toggle.contains(e.target)) {
		setExpanded(false);
	}
	}
});

// Close on escape
document.addEventListener('keydown', function (e) {
	if (e.key === 'Escape') setExpanded(false);
});
})();


(function () {
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const applyTheme = (isDark) => {
      if (isDark) document.documentElement.classList.add('dark');
      else document.documentElement.classList.remove('dark');
    };

    const stored = localStorage.getItem('theme');
    if (stored === 'dark') applyTheme(true);
    else if (stored === 'light') applyTheme(false);
    else applyTheme(prefersDark);
})();
