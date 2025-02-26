from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Product
from .forms import ProductForm



# 제품 목록 (검색 + 페이징)
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"
    ordering = ["-created_at"]
    login_url = "/accounts/login/"
    paginate_by = 10  # 한 페이지당 10개씩 표시


# 제품 불러오기 및 정렬
    def get_queryset(self):
        queryset = Product.objects.all()
        sort = self.request.GET.get("sort", "created_at")  # 기본 정렬 필드
        order = self.request.GET.get("order", "desc")  # 기본 정렬 방향

        if sort not in ["name", "created_at"]:
            sort = "created_at"

        if order == "asc":
            queryset = queryset.order_by(sort)  # 오름차순
        else:
            queryset = queryset.order_by(f"-{sort}")  # 내림차순

        search_query = self.request.GET.get("q", "").strip()
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset

# paginator 호출 오류로 페이징 강제 추가
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get("page")
        products = paginator.get_page(page)

        # 빈 행 개수 계산 (최대 10개 유지)
        empty_rows = max(0, self.paginate_by - len(products))

        context["products"] = products
        context["paginator"] = paginator
        context["page_range"] = paginator.page_range  # 페이지 범위 추가
        context["empty_rows"] = range(empty_rows)  # 부족한 빈 행 개수 전달
        context["current_sort"] = self.request.GET.get("sort", "created_at")  # 현재 정렬 필드
        context["current_order"] = self.request.GET.get("order", "desc")  # 현재 정렬 방향
        return context


# 제품 생성
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "store/product_form.html"
    success_url = reverse_lazy("product_list")
    login_url = "/accounts/login/"


# 제품 수정
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "store/product_form.html"
    success_url = reverse_lazy("product_list")
    login_url = "/accounts/login/"


# 제품 삭제
@method_decorator(csrf_exempt, name="dispatch")
class ProductDeleteView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return JsonResponse({"message": "삭제 성공"}, status=200)
