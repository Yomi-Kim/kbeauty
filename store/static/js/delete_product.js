document.addEventListener("DOMContentLoaded", function () {
    let productIdToDelete = null;

    // 제품명 길이 제한 함수 (10자 이상이면 "...")
    function trimProductName(name, maxLength) {
        return name.length > maxLength ? name.substring(0, maxLength) + "..." : name;
    }

    // CSRF토큰 
    function getCSRFToken() {
        return document.querySelector("input[name=csrfmiddlewaretoken]")?.value || "";
    }

    // 삭제 버튼 클릭시
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function () {
            productIdToDelete = this.getAttribute("data-product-id");
            let productName = this.getAttribute("data-product-name");
            let trimmedName = trimProductName(productName, 10);

            let nameElement = document.getElementById("delete-product-name");
            nameElement.textContent = trimmedName;
            nameElement.setAttribute("title", productName);
        });
    });


    // 삭제 확인 버튼 클릭시
    document.getElementById("confirm-delete").addEventListener("click", function () {
        if (productIdToDelete) {
            const csrftoken = getCSRFToken();

            fetch(`/products/${productIdToDelete}/delete/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({})
            })
                .then(response => {
                    if (response.ok) {
                        document.getElementById(`product-${productIdToDelete}`).remove();
                        alert("삭제되었습니다.")
                        location.reload();
                    } else {
                        alert("삭제 실패! 다시 시도해주세요.");
                    }
                })
                .catch(error => {
                    alert("삭제 요청 중 오류가 발생했습니다.");
                });
        }
    });



});
