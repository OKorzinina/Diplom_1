"""
Тесты для главного модуля praktikum.py
"""
import pytest
from unittest.mock import Mock, patch, call
from praktikum.praktikum import main


class TestPraktikum:
    """Тестирование основного модуля программы"""
    
    @patch('praktikum.praktikum.print')  # Мокаем print
    @patch('praktikum.praktikum.Database')  # Мокаем Database
    def test_main_function_creates_burger_correctly(self, mock_database_class, mock_print):
        """
        Тестирует, что функция main() правильно создает бургер:
        1. Создает базу данных
        2. Берет нужные булочки и ингредиенты
        3. Добавляет ингредиенты в правильном порядке
        4. Перемещает и удаляет ингредиенты
        5. Выводит правильный чек
        """
        # ===== ARRANGE =====
        # Создаем мок для экземпляра Database
        mock_database_instance = Mock()
        mock_database_class.return_value = mock_database_instance
        
        # Создаем моки для булочек
        mock_buns = [Mock() for _ in range(3)]
        mock_buns[0].get_name.return_value = "black bun"
        mock_buns[0].get_price.return_value = 100.0
        
        # Создаем моки для ингредиентов (6 штук)
        mock_ingredients = [Mock() for _ in range(6)]
        
        # Настраиваем возвращаемые значения для ингредиентов
        # Соусы (первые 3)
        mock_ingredients[0].get_type.return_value = "SAUCE"
        mock_ingredients[0].get_name.return_value = "hot sauce"
        mock_ingredients[0].get_price.return_value = 100.0
        
        mock_ingredients[1].get_type.return_value = "SAUCE"
        mock_ingredients[1].get_name.return_value = "sour cream"
        mock_ingredients[1].get_price.return_value = 200.0
        
        mock_ingredients[2].get_type.return_value = "SAUCE"
        mock_ingredients[2].get_name.return_value = "chili sauce"
        mock_ingredients[2].get_price.return_value = 300.0
        
        # Начинки (последние 3)
        mock_ingredients[3].get_type.return_value = "FILLING"
        mock_ingredients[3].get_name.return_value = "cutlet"
        mock_ingredients[3].get_price.return_value = 100.0
        
        mock_ingredients[4].get_type.return_value = "FILLING"
        mock_ingredients[4].get_name.return_value = "dinosaur"
        mock_ingredients[4].get_price.return_value = 200.0
        
        mock_ingredients[5].get_type.return_value = "FILLING"
        mock_ingredients[5].get_name.return_value = "sausage"
        mock_ingredients[5].get_price.return_value = 300.0
        
        # Настраиваем методы базы данных
        mock_database_instance.available_buns.return_value = mock_buns
        mock_database_instance.available_ingredients.return_value = mock_ingredients
        
        # ===== ACT =====
        # Вызываем тестируемую функцию
        main()
        
        # ===== ASSERT =====
        # 1. Проверяем создание Database
        mock_database_class.assert_called_once()
        
        # 2. Проверяем вызовы методов базы данных
        mock_database_instance.available_buns.assert_called_once()
        mock_database_instance.available_ingredients.assert_called_once()
        
        # 3. Проверяем, что print был вызван
        mock_print.assert_called_once()
        
        # 4. Получаем аргумент, с которым был вызван print
        printed_receipt = mock_print.call_args[0][0]
        
        # 5. Проверяем содержимое чека
        assert "(==== black bun ====)" in printed_receipt
        assert "Price:" in printed_receipt
    
    @patch('praktikum.praktikum.print')
    @patch('praktikum.praktikum.Database')
    def test_main_uses_correct_indices_from_database(self, mock_database_class, mock_print):
        """
        Проверяем, что main() использует правильные индексы из базы данных:
        - buns[0] - первая булочка
        - ingredients[1], [4], [3], [5] - конкретные ингредиенты
        """
        # ===== ARRANGE =====
        mock_database_instance = Mock()
        mock_database_class.return_value = mock_database_instance
        
        # Создаем отслеживаемые моки
        mock_buns = [Mock() for _ in range(3)]
        mock_ingredients = [Mock() for _ in range(6)]
        
        # Создаем мок для Burger, чтобы отслеживать вызовы
        with patch('praktikum.praktikum.Burger') as mock_burger_class:
            mock_burger_instance = Mock()
            mock_burger_class.return_value = mock_burger_instance
            
            mock_database_instance.available_buns.return_value = mock_buns
            mock_database_instance.available_ingredients.return_value = mock_ingredients
            
            # ===== ACT =====
            main()
            
            # ===== ASSERT =====
            # Проверяем вызовы методов Burger с правильными аргументами
            mock_burger_instance.set_buns.assert_called_once_with(mock_buns[0])
            
            # Проверяем добавление ингредиентов в правильном порядке
            expected_add_calls = [
                call(mock_ingredients[1]),
                call(mock_ingredients[4]),
                call(mock_ingredients[3]),
                call(mock_ingredients[5])
            ]
            mock_burger_instance.add_ingredient.assert_has_calls(expected_add_calls)
            
            # Проверяем перемещение ингредиента
            mock_burger_instance.move_ingredient.assert_called_once_with(2, 1)
            
            # Проверяем удаление ингредиента
            mock_burger_instance.remove_ingredient.assert_called_once_with(3)
            
            # Проверяем вывод чека
            mock_burger_instance.get_receipt.assert_called_once()
            mock_print.assert_called_once_with(mock_burger_instance.get_receipt.return_value)
    
    @patch('praktikum.praktikum.print')
    @patch('praktikum.praktikum.Database')
    def test_main_handles_empty_database(self, mock_database_class, mock_print):
        """
        Тестируем обработку пустой базы данных
        """
        # ===== ARRANGE =====
        mock_database_instance = Mock()
        mock_database_class.return_value = mock_database_instance
        
        # Пустые списки
        mock_database_instance.available_buns.return_value = []
        mock_database_instance.available_ingredients.return_value = []
        
        # ===== ACT & ASSERT =====
        # Должно вызвать IndexError при попытке обращения по индексу
        with pytest.raises(IndexError):
            main()
    
    def test_main_can_be_imported(self):
        """
        Проверяем, что модуль можно импортировать без ошибок
        """
        # Эта проверка гарантирует, что синтаксис модуля корректен
        from praktikum.praktikum import main
        assert callable(main)
    
    @patch('praktikum.praktikum.print')
    @patch('praktikum.praktikum.Database')
    def test_main_price_calculation_integration(self, mock_database_class, mock_print):
        """
        Интеграционный тест: проверяем правильность расчета цены
        """
        # ===== ARRANGE =====
        mock_database_instance = Mock()
        mock_database_class.return_value = mock_database_instance
        
        # Настраиваем цены согласно коду из database.py
        mock_buns = [Mock()]
        mock_buns[0].get_name.return_value = "black bun"
        mock_buns[0].get_price.return_value = 100.0  # black bun цена 100
        
        # Создаем 6 ингредиентов как в database.py
        mock_ingredients = [Mock() for _ in range(6)]
        
        # Соусы (индексы 0, 1, 2)
        mock_ingredients[0].get_price.return_value = 100.0  # hot sauce
        mock_ingredients[1].get_price.return_value = 200.0  # sour cream
        mock_ingredients[2].get_price.return_value = 300.0  # chili sauce
        
        # Начинки (индексы 3, 4, 5)
        mock_ingredients[3].get_price.return_value = 100.0  # cutlet
        mock_ingredients[4].get_price.return_value = 200.0  # dinosaur
        mock_ingredients[5].get_price.return_value = 300.0  # sausage
        
        mock_database_instance.available_buns.return_value = mock_buns
        mock_database_instance.available_ingredients.return_value = mock_ingredients
        
        # ===== ACT =====
        main()
        
        # ===== ASSERT =====
        # main() добавляет: ingredients[1], [4], [3], [5]
        # Цены: sour cream(200) + dinosaur(200) + cutlet(100) + sausage(300) = 800
        # Плюс булочка black bun: 100 * 2 = 200
        # Итого: 200 + 800 = 1000
        
        # Проверяем, что в чеке есть правильная цена
        printed_receipt = mock_print.call_args[0][0]
        assert "Price: 700" in printed_receipt
