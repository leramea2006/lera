document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();
    alert("Thank you for reaching out, " + document.getElementById("name").value + "!");
});

// Example blog posts
const posts = [
    { title: "The Importance of Mindfulness", content: "Mindfulness can significantly enhance your well-being..." },
    { title: "Building Resilience", content: "Resilience is essential for facing life's challenges..." }
];

const postsContainer = document.getElementById("posts");
posts.forEach(post => {
    const postElement = document.createElement("div");
    postElement.innerHTML = `<h3>${post.title}</h3><p>${post.content}</p>`;
    postsContainer.appendChild(postElement);
});
