# 定义版本号和后缀变量
VERSION := $(shell python -c "from weeeTest import get_version; print(get_version)")
Project := $(shell pwd)

# 定义 version 目标，输出版本号和后缀信息
.PHONY: version
version:
	@echo $(VERSION)
	exit 0

init:
	pip install -r requirements.txt
	exit 0

clean:
	@echo " 项目路径 $(Project)"
	find $(Project) -type d -name "reports" -exec rm -rf {} +
	find $(Project) -type d \( -name "__pycache__" -and ! -wholename "$(Project)/venv/*" \) -exec rm -rf {} +
	find $(Project) -type d -name ".pytest_cache" -exec rm -rf {} +
	find $(Project) -type d -name "demo_test" -exec rm -rf {} +
	find $(Project) -type d -name "dist" -exec rm -rf {} +

test:
	make publish
	# 安装weeeTest
	pip install weeeTest==$(VERSION) -i https://maven.sayweee.net/repository/pypi-public/simple
	# 查看版本
	weeeTest --version
	# 创建demo项目
	weeeTest -p demo_test
	# 运行demo项目
	cd demo_test && pwd && python run.py
	# 删除demo项目
	rm -rf demo_test && pwd && rm -rf reports
	# 卸载weeeTest
	pip uninstall weeeTest -y

	exit 0

flake8:
	flake8 --ignore=E501,F401,E128,E402,E731,F821 weeeTest


publish:
	make clean
	pip install 'twine>=1.5.0'
	pip install wheel
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg weeeTest.egg-info reports .pytest_cache
	exit 0

release:
	@echo "Current version is $(VERSION)"
ifndef SUFFIX
	@echo "release"
	@read -p "Are you sure you want to perform the release? (yes/no) " confirm; \
	if [ "$$confirm" != "yes" ]; then \
		echo "continue release"; \
		git tag $(VERSION); \
		git push origin $(VERSION); \
		make publish; \
	fi
	exit 0

else
	@echo "git tag $(VERSION)"
	@read -p "Are you sure you want to perform the git tag? (yes/no) " confirm; \
	if [ "$$confirm" != "no" ]; then \
		echo "continue git tag"; \
		git tag $(VERSION); \
		git push origin $(VERSION); \
	fi
	exit 0

endif