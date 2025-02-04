document
  .getElementById("insightsForm")
  .addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();

    document.getElementById("results").innerHTML = `
        <div class="text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
    `;

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/pages/${username}/scrape`
      );

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();

      document.getElementById("results").innerHTML = `
            <h2>Page Insights</h2>
            <div class="card">
                <div class="card-body">
                    <div class="d-flex justify-content-center">
                        <img src="${data.profile_pic}" class="img-thumbnail" alt="${data.name}">
                    </div>
                    <p class="mt-3"><strong>Name:</strong> ${data.name}</p>
                    <p><strong>URL:</strong> <a href="${data.url}" target="_blank">${data.url}</a></p>
                    <p><strong>Followers:</strong> ${data.followers}</p>
                    <p><strong>Likes:</strong> ${data.likes}</p>
                </div>
            </div>
        `;
    } catch (error) {
      document.getElementById("results").innerHTML = `
            <div class="alert alert-danger" role="alert">
                An error occurred: ${error.message}
            </div>
        `;
    }
  });
