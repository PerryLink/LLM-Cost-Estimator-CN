# Contributing to llm-cost-estimator-cn

Thank you for your interest in this project!

## Project Status

This is a **personally maintained project**. Currently, all development is done by the project owner ([@PerryLink](https://github.com/PerryLink)). External contributions are welcome but may take time to review.

---

## Reporting Issues

If you find a bug or have a feature request, please [open an issue](https://github.com/PerryLink/llm-cost-estimator-cn/issues) and include:

- A clear and descriptive title
- Steps to reproduce the problem (for bugs)
- Expected behavior vs. actual behavior
- Your Python version and operating system
- Any relevant error messages or stack traces

---

## Development Setup

**Prerequisites:** Python 3.8+, pip

```bash
# 1. Fork and clone the repository
git clone https://github.com/PerryLink/llm-cost-estimator-cn.git
cd llm-cost-estimator-cn

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# or
.venv\Scripts\activate           # Windows

# 3. Install in editable mode with dev dependencies
pip install -e ".[dev]"

# 4. Verify the setup
llm-cost-estimator-cn --help
pytest tests/
```

---

## Code Style

This project follows [PEP 8](https://peps.python.org/pep-0008/) and uses the following tools:

| Tool | Purpose | Command |
|------|---------|---------|
| [Black](https://github.com/psf/black) | Code formatting | `black src/ tests/` |
| [Ruff](https://github.com/astral-sh/ruff) | Linting | `ruff check src/ tests/` |
| [pytest](https://pytest.org/) | Testing | `pytest tests/` |

Please run all three before submitting a pull request:

```bash
black src/ tests/
ruff check src/ tests/
pytest tests/
```

---

## Pull Request Process

1. **Fork** the repository and create a branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and ensure:
   - Code passes `black` formatting and `ruff` linting checks
   - Existing tests still pass (`pytest tests/`)
   - New functionality includes appropriate tests

3. **Commit** with a clear message describing what changed and why:
   ```bash
   git commit -m "feat: add support for XYZ model pricing"
   ```

4. **Push** to your fork and open a pull request against `main`.

5. The pull request description should include:
   - What problem this solves
   - How it was tested
   - Any relevant notes for the reviewer

---

## Contact

For questions or suggestions beyond GitHub issues, you can reach the maintainer at: novelnexusai@outlook.com

---

# 贡献指南

感谢您对本项目的关注！

## 项目状态

这是一个**个人维护的项目**，目前所有开发工作由项目所有者（[@PerryLink](https://github.com/PerryLink)）独立完成。欢迎外部贡献，但回复和合并可能需要一些时间。

---

## 报告问题

如果您发现了 bug 或有功能建议，请[提交 Issue](https://github.com/PerryLink/llm-cost-estimator-cn/issues)，并提供以下信息：

- 清晰的标题
- 复现步骤（针对 bug）
- 预期行为与实际行为的对比
- 您的 Python 版本和操作系统
- 相关的错误信息或堆栈跟踪

---

## 开发环境搭建

**前置条件：** Python 3.8+、pip

```bash
# 1. Fork 并克隆仓库
git clone https://github.com/PerryLink/llm-cost-estimator-cn.git
cd llm-cost-estimator-cn

# 2. 创建虚拟环境
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# 或
.venv\Scripts\activate           # Windows

# 3. 以可编辑模式安装（包含开发依赖）
pip install -e ".[dev]"

# 4. 验证安装
llm-cost-estimator-cn --help
pytest tests/
```

---

## 代码规范

本项目遵循 [PEP 8](https://peps.python.org/pep-0008/) 规范，并使用以下工具：

| 工具 | 用途 | 命令 |
|------|------|------|
| [Black](https://github.com/psf/black) | 代码格式化 | `black src/ tests/` |
| [Ruff](https://github.com/astral-sh/ruff) | 代码检查 | `ruff check src/ tests/` |
| [pytest](https://pytest.org/) | 测试 | `pytest tests/` |

提交 Pull Request 前请运行全部三项检查：

```bash
black src/ tests/
ruff check src/ tests/
pytest tests/
```

---

## Pull Request 流程

1. **Fork** 仓库，并从 `main` 创建新分支：
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **进行修改**，并确保：
   - 代码通过 `black` 格式化和 `ruff` 检查
   - 现有测试全部通过（`pytest tests/`）
   - 新功能包含相应的测试用例

3. **提交**，使用清晰的提交信息描述变更内容和原因：
   ```bash
   git commit -m "feat: 新增 XYZ 模型定价支持"
   ```

4. **推送**到您的 Fork，并向 `main` 提交 Pull Request。

5. Pull Request 描述中请注明：
   - 解决了什么问题
   - 如何进行测试
   - 对审阅者的其他说明

---

## 联系方式

如有超出 Issue 范围的问题或建议，可通过邮件联系维护者：novelnexusai@outlook.com
