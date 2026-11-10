INSERT INTO `play_store`.`accounts` (`id`, `email`, `password_hash`, `name`, `is_developer`, `country`, `created_at`) VALUES
(1,  'oleksandr.melnyk@example.com', SHA2('pwd_01', 256), 'Oleksandr Melnyk',   0, 'Ukraine',        '2023-01-15 10:20:00'),
(2,  'iryna.kovalenko@example.com',  SHA2('pwd_02', 256), 'Iryna Kovalenko',    0, 'Ukraine',        '2023-02-03 14:05:00'),
(3,  'john.smith@example.com',       SHA2('pwd_03', 256), 'John Smith',         0, 'United States',  '2023-02-20 09:30:00'),
(4,  'anna.nowak@example.com',       SHA2('pwd_04', 256), 'Anna Nowak',         0, 'Poland',         '2023-03-11 18:45:00'),
(5,  'lukas.meyer@example.com',      SHA2('pwd_05', 256), 'Lukas Meyer',        0, 'Germany',        '2023-04-02 12:00:00'),
(6,  'dev@pixelforge.example.com',   SHA2('pwd_06', 256), 'PixelForge Admin',   1, 'United States',  '2022-06-01 08:00:00'),
(7,  'dev@greenleaf.example.com',    SHA2('pwd_07', 256), 'GreenLeaf Admin',    1, 'Germany',        '2022-07-12 09:10:00'),
(8,  'dev@softbridge.example.com',   SHA2('pwd_08', 256), 'SoftBridge Admin',   1, 'Ukraine',        '2022-08-23 11:25:00'),
(9,  'dev@nordapps.example.com',     SHA2('pwd_09', 256), 'NordApps Admin',     1, 'Sweden',         '2022-09-05 13:40:00'),
(10, 'dev@bluewave.example.com',     SHA2('pwd_10', 256), 'BlueWave Admin',     1, 'Canada',         '2022-10-17 15:55:00'),
(11, 'dev@kodiak.example.com',       SHA2('pwd_11', 256), 'Kodiak Admin',       1, 'Poland',         '2022-11-28 10:15:00'),
(12, 'dev@sunrise.example.com',      SHA2('pwd_12', 256), 'Sunrise Admin',      1, 'Japan',          '2023-01-09 07:30:00'),
(13, 'dev@zenith.example.com',       SHA2('pwd_13', 256), 'Zenith Admin',       1, 'United Kingdom', '2023-01-30 16:20:00'),
(14, 'dev@mapleapps.example.com',    SHA2('pwd_14', 256), 'Maple Admin',        1, 'Canada',         '2023-02-14 12:45:00'),
(15, 'dev@carpathia.example.com',    SHA2('pwd_15', 256), 'Carpathia Admin',    1, 'Ukraine',        '2023-03-01 09:00:00');

INSERT INTO `play_store`.`devices` (`id`, `model`, `os_version`) VALUES
(1,  'Pixel 7',           '14'),
(2,  'Pixel 8 Pro',       '15'),
(3,  'Galaxy S23',        '14'),
(4,  'Galaxy A54',        '13'),
(5,  'Xiaomi 13T',        '14'),
(6,  'OnePlus 11',        '14'),
(7,  'Redmi Note 12',     '13'),
(8,  'Motorola Edge 40',  '14'),
(9,  'Nothing Phone 2',   '14'),
(10, 'Galaxy Tab S9',     '14'),
(11, 'Lenovo Tab P12',    '13'),
(12, 'Pixel 6a',          '13');

INSERT INTO `play_store`.`accounts_devices` (`account_id`, `device_id`) VALUES
(1, 1), (1, 10), (2, 3), (2, 4), (3, 2), (3, 12),
(4, 5), (4, 7),  (5, 6), (5, 9), (6, 8), (7, 11);

INSERT INTO `play_store`.`companies` (`id`, `company_name`, `contact_email`, `developer_account_id`) VALUES
(1,  'PixelForge Studio',  'support@pixelforge.example.com', 6),
(2,  'GreenLeaf Software', 'contact@greenleaf.example.com',  7),
(3,  'SoftBridge',         'hello@softbridge.example.com',   8),
(4,  'NordApps AB',        'info@nordapps.example.com',      9),
(5,  'BlueWave Inc.',      'team@bluewave.example.com',      10),
(6,  'Kodiak Studio',      'office@kodiak.example.com',      11),
(7,  'Sunrise Games',      'support@sunrise.example.com',    12),
(8,  'Zenith Labs',        NULL,                             13),
(9,  'Maple Apps',         'contact@mapleapps.example.com',  14),
(10, 'Carpathia Soft',     'hello@carpathia.example.com',    15);

INSERT INTO `play_store`.`categories` (`id`, `name`) VALUES
(1, 'Games'),
(2, 'Productivity'),
(3, 'Education'),
(4, 'Health & Fitness'),
(5, 'Photography'),
(6, 'Music & Audio'),
(7, 'Finance'),
(8, 'Travel'),
(9, 'Social'),
(10, 'Tools');

INSERT INTO `play_store`.`apps` (`id`, `title`, `caption`, `price`, `currency`, `company_id`) VALUES
(1,  'Pixel Runner',        'Endless runner with retro pixel graphics',     0.00, 'USD', 1),
(2,  'Galaxy Defender',     'Space shooter with online leaderboards',       2.99, 'USD', 1),
(3,  'Leaf Notes',          'Simple and fast note-taking app',              0.00, 'USD', 2),
(4,  'Habit Garden',        'Build habits and grow your virtual garden',    1.99, 'USD', 2),
(5,  'BridgeChat',          'Messenger with end-to-end encryption',         0.00, 'USD', 3),
(6,  'Nord Weather',        'Accurate forecasts for the Nordic region',     0.99, 'EUR', 4),
(7,  'WaveFit',             'Workout planner and activity tracker',         4.99, 'USD', 5),
(8,  'Kodiak Photo Editor', 'Professional photo editing on your phone',     6.99, 'USD', 6),
(9,  'Sunrise Quest',       'Fantasy RPG adventure',                        9.99, 'USD', 7),
(10, 'Zenith Budget',       'Personal finance and budget planner',          3.49, 'EUR', 8),
(11, 'Maple Trails',        'Offline hiking maps and routes',               2.49, 'USD', 9),
(12, 'Carpathian Guide',    'Travel guide to the Carpathian mountains',     0.00, 'USD', 10);

INSERT INTO `play_store`.`apps_versions` (`id`, `app_id`, `version`, `size_bytes`, `created_at`) VALUES
(1,  1,  '1.0.0', 45234176,  '2023-01-10 10:00:00'),
(2,  1,  '1.1.0', 47185920,  '2023-03-05 11:30:00'),
(3,  2,  '1.0.0', 83886080,  '2023-02-01 09:00:00'),
(4,  3,  '1.0.0', 12582912,  '2023-01-10 12:00:00'),
(5,  3,  '2.0.0', 15728640,  '2023-06-15 14:20:00'),
(6,  4,  '1.0.0', 20971520,  '2023-02-18 16:45:00'),
(7,  5,  '3.2.1', 33554432,  '2023-01-25 08:30:00'),
(8,  6,  '1.0.0', 9437184,   '2023-03-12 10:10:00'),
(9,  7,  '1.0.0', 58720256,  '2023-03-25 13:35:00'),
(10, 8,  '2.4.0', 104857600, '2023-05-02 15:00:00'),
(11, 9,  '1.0.0', 629145600, '2023-05-20 17:15:00'),
(12, 10, '1.0.0', 18874368,  '2023-06-01 09:45:00'),
(13, 11, '1.2.0', 72351744,  '2023-06-18 11:00:00'),
(14, 12, '1.0.0', 26214400,  '2023-04-10 12:30:00');

INSERT INTO `play_store`.`apps_discounts` (`id`, `app_id`, `discount_price`, `starts_at`, `ends_at`) VALUES
(1,  2,  1.99, '2023-05-01 00:00:00', '2023-05-15 23:59:59'),
(2,  4,  0.99, '2023-06-01 00:00:00', '2023-06-10 23:59:59'),
(3,  6,  0.49, '2023-04-01 00:00:00', '2023-04-07 23:59:59'),
(4,  7,  2.99, '2023-07-01 00:00:00', '2023-07-31 23:59:59'),
(5,  8,  3.99, '2023-08-01 00:00:00', '2023-08-14 23:59:59'),
(6,  9,  5.99, '2023-09-01 00:00:00', '2023-09-30 23:59:59'),
(7,  10, 1.99, '2023-06-20 00:00:00', '2023-06-27 23:59:59'),
(8,  11, 1.49, '2023-07-10 00:00:00', '2023-07-20 23:59:59'),
(9,  9,  7.99, '2023-11-24 00:00:00', '2023-11-30 23:59:59'),
(10, 7,  3.99, '2023-12-20 00:00:00', '2023-12-31 23:59:59');

INSERT INTO `play_store`.`apps_categories` (`app_id`, `category_id`) VALUES
(1, 1), (2, 1), (3, 2), (4, 2), (4, 4), (5, 9), (6, 8),
(7, 4), (8, 5), (9, 1), (10, 7), (11, 8), (11, 4), (12, 8);

INSERT INTO `play_store`.`installations` (`app_id`, `device_id`, `installed_at`) VALUES
(1,  1,  '2023-01-16 10:30:00'),
(1,  3,  '2023-02-05 15:00:00'),
(3,  1,  '2023-01-16 10:45:00'),
(3,  2,  '2023-02-21 09:50:00'),
(5,  5,  '2023-03-12 19:00:00'),
(5,  3,  '2023-02-04 14:20:00'),
(2,  2,  '2023-03-01 20:15:00'),
(6,  4,  '2023-04-03 07:40:00'),
(7,  5,  '2023-04-05 18:30:00'),
(8,  12, '2023-05-10 12:10:00'),
(9,  6,  '2023-06-02 21:00:00'),
(10, 3,  '2023-06-22 08:25:00'),
(11, 9,  '2023-07-12 16:35:00'),
(12, 7,  '2023-04-20 13:00:00'),
(4, 1,  '2023-06-30 07:10:00'),
(2, 4,  '2023-05-20 20:30:00');

INSERT INTO `play_store`.`payment_cards` (`id`, `account_id`, `token`, `card_brand`, `exp_date`, `last4`) VALUES
(1,  1, 'tok_1A2b3C4d5E6f', 'Visa',             '2028-08-31', '4242'),
(2,  1, 'tok_2B3c4D5e6F7g', 'Mastercard',       '2027-02-28', '5555'),
(3,  2, 'tok_3C4d5E6f7G8h', 'Visa',             '2028-11-30', '1881'),
(4,  2, 'tok_4D5e6F7g8H9i', 'Mastercard',       '2029-12-31', '4444'),
(5,  3, 'tok_5E6f7G8h9I0j', 'Visa',             '2027-05-31', '1111'),
(6,  3, 'tok_6F7g8H9i0J1k', 'American Express', '2028-09-30', '0005'),
(7,  4, 'tok_7G8h9I0j1K2l', 'Mastercard',       '2027-01-31', '9424'),
(8,  4, 'tok_8H9i0J1k2L3m', 'Visa',             '2029-06-30', '0119'),
(9,  5, 'tok_9I0j1K2l3M4n', 'Visa',             '2028-03-31', '6781'),
(10, 5, 'tok_0J1k2L3m4N5o', 'Mastercard',       '2027-10-31', '2222');

INSERT INTO `play_store`.`reviews` (`account_id`, `app_id`, `rating`, `comment`, `created_at`) VALUES
(1, 1,  4.5, 'Fun and addictive, great pixel art!',      '2023-02-10 20:00:00'),
(3, 3,  5.0, 'Best minimalist notes app I have used.',   '2023-03-01 09:15:00'),
(3, 2,  4.0, 'Good shooter, a bit short.',               '2023-03-10 22:30:00'),
(4, 5,  4.5, 'Fast and reliable messenger.',             '2023-03-20 17:45:00'),
(2, 6,  3.5, 'Accurate, but the UI is plain.',           '2023-04-10 08:00:00'),
(4, 7,  4.0, 'Helps me stay on track with workouts.',    '2023-05-01 07:20:00'),
(3, 8,  5.0, 'Powerful editor, worth every cent.',       '2023-05-20 13:10:00'),
(5, 9,  4.5, 'Great story and music.',                   '2023-06-20 21:40:00'),
(2, 10, 4.0, 'Simple budget planning.',                  '2023-07-01 10:30:00'),
(5, 11, 5.0, NULL,                                       '2023-07-25 18:00:00'),
(1, 4,  3.5, 'Nice idea, needs more plants.',            '2023-06-25 12:00:00'),
(4, 2,  4.0, 'Cheap with the discount!',                 '2023-05-12 20:10:00');

INSERT INTO `play_store`.`bills` (`currency`, `amount_paid`, `app_id`, `payment_card_id`, `paid_at`, `discount_id`, `account_id`) VALUES
('USD', 2.99, 2,  5,  '2023-03-01 20:10:00', NULL, 3),
('EUR', 0.49, 6,  3,  '2023-04-03 07:35:00', 3,    2),
('USD', 4.99, 7,  7,  '2023-04-05 18:25:00', NULL, 4),
('USD', 6.99, 8,  6,  '2023-05-10 12:05:00', NULL, 3),
('USD', 9.99, 9,  9,  '2023-06-02 20:55:00', NULL, 5),
('EUR', 1.99, 10, 4,  '2023-06-22 08:20:00', 7,    2),
('USD', 1.49, 11, 10, '2023-07-12 16:30:00', 8,    5),
('USD', 0.99, 4,  1,  '2023-06-05 10:00:00', 2,    1),
('USD', 1.99, 2,  8,  '2023-05-05 19:40:00', 1,    4),
('USD', 2.99, 7,  2,  '2023-07-15 11:20:00', 4,    1);

INSERT INTO `play_store`.`library` (`app_id`, `account_id`, `app_data`, `last_opened_at`) VALUES
(1,  1, '{"level": 12, "high_score": 15400}',                 '2023-03-20 21:00:00'),
(3,  3, '{"notes_count": 34, "theme": "dark"}',               '2023-07-01 08:00:00'),
(2,  3, '{"level": 5, "ship": "falcon"}',                     '2023-03-15 22:00:00'),
(2,  4, '{"level": 8, "ship": "phoenix"}',                    '2023-05-20 20:30:00'),
(5,  4, '{"chats": 7, "notifications": true}',                '2023-08-01 18:00:00'),
(6,  2, '{"units": "metric", "city": "Lviv"}',                '2023-08-12 07:30:00'),
(7,  4, '{"workouts_done": 21, "goal": "endurance"}',         '2023-08-15 06:50:00'),
(7,  1, '{"workouts_done": 9, "goal": "strength"}',           NULL),
(8,  3, '{"filters_saved": 4}',                               '2023-06-01 19:45:00'),
(9,  5, '{"level": 17, "gold": 2300}',                        '2023-07-30 22:10:00'),
(10, 2, '{"currency": "EUR", "budgets": 3}',                  '2023-07-05 09:00:00'),
(11, 5, '{"saved_routes": 6}',                                '2023-08-02 10:20:00'),
(4,  1, '{"habits": 5, "streak": 14}',                        '2023-06-30 07:10:00'),
(1,  2, '{"level": 3, "high_score": 4200}',                   '2023-02-10 21:00:00'),
(3,  1, '{"notes_count": 12, "theme": "light"}',              '2023-02-01 08:30:00'),
(5,  2, '{"chats": 3, "notifications": false}',               '2023-02-20 19:00:00'),
(12, 4, '{"saved_guides": 2}',                                '2023-05-02 09:10:00');