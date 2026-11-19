START TRANSACTION;

INSERT INTO `play_store`.`accounts` (`id`, `email`, `password_hash`, `name`, `created_at`, `deleted_at`) VALUES
(1,  'olena.kovalenko@example.com', SHA2('demo_password_1', 256),  'Олена Коваленко',  '2025-01-15 10:00:00', NULL),
(2,  'andrii.shevchenko@example.com', SHA2('demo_password_2', 256),  'Андрій Шевченко',  '2025-02-03 12:30:00', NULL),
(3,  'maria.bondar@example.com',    SHA2('demo_password_3', 256),  'Марія Бондар',     '2025-02-20 08:45:00', NULL),
(4,  'taras.melnyk@example.com',    SHA2('demo_password_4', 256),  'Тарас Мельник',    '2025-03-11 16:10:00', NULL),
(5,  'iryna.tkachenko@example.com', SHA2('demo_password_5', 256),  'Ірина Ткаченко',   '2025-04-02 09:20:00', NULL),
(6,  'bohdan.kravchuk@example.com', SHA2('demo_password_6', 256),  'Богдан Кравчук',   '2025-05-18 14:05:00', NULL),
(7,  'sofiia.lysenko@example.com',  SHA2('demo_password_7', 256),  'Софія Лисенко',    '2025-06-07 11:15:00', NULL),
(8,  'yurii.oliinyk@example.com',   SHA2('demo_password_8', 256),  'Юрій Олійник',     '2025-07-29 19:40:00', NULL),
(9,  'daryna.savchenko@example.com', SHA2('demo_password_9', 256),  'Дарина Савченко',  '2025-09-14 07:55:00', NULL),
(10, 'oleh.petrenko@example.com',   SHA2('demo_password_10', 256), 'Олег Петренко',    '2025-10-30 13:25:00', NULL),
(11, 'vasyl.hrytsenko@example.com',  SHA2('demo_password_11', 256), 'Василь Гриценко',  '2025-01-20 09:00:00', NULL),
(12, 'natalia.moroz@example.com',    SHA2('demo_password_12', 256), 'Наталія Мороз',    '2025-02-10 15:20:00', NULL),
(13, 'viktor.zinchenko@example.com', SHA2('demo_password_13', 256), 'Віктор Зінченко',  '2025-03-05 18:45:00', NULL),
(14, 'kateryna.polishchuk@example.com', SHA2('demo_password_14', 256), 'Катерина Поліщук', '2025-04-18 10:10:00', NULL),
(15, 'mykola.rudenko@example.com',   SHA2('demo_password_15', 256), 'Микола Руденко',   '2025-05-25 21:30:00', NULL);

INSERT INTO `play_store`.`devices` (`id`, `model`, `os_version`) VALUES
(1,  'Pixel 7',          'Android 14'),
(2,  'Pixel 8',          'Android 14'),
(3,  'Galaxy S23',       'Android 14'),
(4,  'Galaxy S24',       'Android 15'),
(5,  'Galaxy A54',       'Android 13'),
(6,  'Xiaomi 13',        'Android 14'),
(7,  'OnePlus 11',       'Android 14'),
(8,  'Redmi Note 12',    'Android 13'),
(9,  'Motorola Edge 40', 'Android 13'),
(10, 'Pixel 6a',         'Android 13');

INSERT INTO `play_store`.`accounts_devices` (`account_id`, `device_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 9),
(11, 1),
(11, 4),
(12, 5),
(13, 6),
(14, 7),
(15, 8);

INSERT INTO `play_store`.`companies` (`id`, `company_name`, `contact_email`, `developer_id`) VALUES
(1,  'Nova Labs',          'support@novalabs.example.com',  1),
(2,  'PixelForge Studio',  'hello@pixelforge.example.com',  2),
(3,  'GreenLeaf Software', NULL,                            3),
(4,  'Lviv Apps',          'team@lvivapps.example.com',     4),
(5,  'Karpaty Games',      'info@karpaty.example.com',      5),
(6,  'BlueWave Media',     NULL,                            6),
(7,  'SkyNet Tools',       'contact@skynet.example.com',    7),
(8,  'Orbit Education',    'learn@orbit.example.com',       8),
(9,  'FitLife Digital',    'help@fitlife.example.com',      9),
(10, 'CodeCraft Ltd',      'dev@codecraft.example.com',     10);

INSERT INTO `play_store`.`categories` (`id`, `name`) VALUES
(1,  'Games'),
(2,  'Education'),
(3,  'Productivity'),
(4,  'Tools'),
(5,  'Health & Fitness'),
(6,  'Music & Audio'),
(7,  'Photography'),
(8,  'Social'),
(9,  'Finance'),
(10, 'Travel & Local');

INSERT INTO `play_store`.`apps` (`id`, `title`, `package_name`, `caption`, `company_id`, `status`) VALUES
(1,  'Nova Notes',       'com.novalabs.notes',     'Швидкі нотатки з синхронізацією між пристроями',  1,  'published'),
(2,  'PixelPaint',       'com.pixelforge.paint',   'Простий та потужний графічний редактор',          2,  'published'),
(3,  'Garden Planner',   'com.greenleaf.garden',   NULL,                                              3,  'published'),
(4,  'Lviv Transit',     'com.lvivapps.transit',   'Розклад громадського транспорту Львова',          4,  'published'),
(5,  'Carpathian Quest', 'com.karpaty.quest',      'Пригодницька гра в Карпатах',                     5,  'published'),
(6,  'BlueWave Player',  'com.bluewave.player',    'Музичний плеєр з еквалайзером',                   6,  'published'),
(7,  'SkyNet Cleaner',   'com.skynet.cleaner',     'Очищення пам''яті пристрою',                      7,  'suspended'),
(8,  'Orbit Lingo',      'com.orbit.lingo',        'Вивчення іноземних мов щодня',                    8,  'published'),
(9,  'FitLife Tracker',  'com.fitlife.tracker',    NULL,                                              9,  'unpublished'),
(10, 'CodeCraft IDE',    'com.codecraft.ide',      'Мобільне середовище для програмування',           10, 'published');

INSERT INTO `play_store`.`apps_categories` (`app_id`, `category_id`) VALUES
(1,  3),
(2,  7),
(3,  4),
(4,  10),
(5,  1),
(6,  6),
(7,  4),
(8,  2),
(9,  5),
(10, 3);

INSERT INTO `play_store`.`apps_versions` (`id`, `app_id`, `version`, `size_bytes`, `created_at`) VALUES
(1,  1,  '1.0.0', 15728640,  '2025-03-01 10:00:00'),
(2,  1,  '1.1.0', 16777216,  '2025-06-15 10:00:00'),
(3,  2,  '2.3.1', 52428800,  '2025-04-10 09:30:00'),
(4,  3,  '1.0.5', 9437184,   '2025-05-05 12:00:00'),
(5,  4,  '3.2.0', 21495808,  '2025-07-20 08:00:00'),
(6,  5,  '0.9.8', 314572800, '2025-08-12 17:45:00'),
(7,  6,  '4.5.2', 38797312,  '2025-09-01 11:20:00'),
(8,  8,  '1.4.0', 27262976,  '2025-09-25 15:10:00'),
(9,  7,  '2.0.0', 12582912,  '2025-10-03 13:00:00'),
(10, 10, '5.0.1', 73400320,  '2025-10-28 18:30:00');

INSERT INTO `play_store`.`installations` (`id`, `device_id`, `app_version_id`, `installed_at`, `updated_at`) VALUES
(1,  1,  2,  '2025-06-20 10:00:00', '2025-07-01 09:00:00'),
(2,  2,  3,  '2025-04-15 11:30:00', NULL),
(3,  3,  4,  '2025-05-10 14:00:00', NULL),
(4,  4,  5,  '2025-07-25 08:15:00', '2025-08-02 19:00:00'),
(5,  5,  6,  '2025-08-15 20:00:00', NULL),
(6,  6,  7,  '2025-09-05 12:45:00', NULL),
(7,  7,  8,  '2025-09-30 16:20:00', '2025-10-10 10:10:00'),
(8,  8,  9,  '2025-10-05 09:05:00', NULL),
(9,  9,  10, '2025-10-30 21:00:00', NULL),
(10, 10, 1,  '2025-03-05 07:30:00', '2025-06-20 07:30:00');

INSERT INTO `play_store`.`library` (`id`, `app_id`, `account_id`, `last_opened_at`, `added_at`, `data_ref`) VALUES
(1,  1,  11, '2025-11-01 08:00:00', '2025-03-10 10:00:00', 'cloud://backup/11/1'),
(2,  2,  12, '2025-10-20 19:30:00', '2025-04-12 12:00:00', 'cloud://backup/12/2'),
(3,  3,  13, NULL,                  '2025-05-08 09:00:00', NULL),
(4,  4,  14, '2025-11-10 07:45:00', '2025-07-22 15:00:00', 'cloud://backup/14/4'),
(5,  5,  15, '2025-11-12 22:10:00', '2025-08-14 18:00:00', 'cloud://backup/15/5'),
(6,  6,  11, '2025-10-29 13:00:00', '2025-09-03 11:00:00', NULL),
(7,  8,  12, '2025-11-14 06:50:00', '2025-09-27 16:30:00', 'cloud://backup/12/8'),
(8,  10, 13, '2025-11-05 17:20:00', '2025-10-30 21:10:00', 'cloud://backup/13/10'),
(9,  3,  14, NULL,                  '2025-11-02 10:40:00', NULL),
(10, 5,  1,  '2025-11-08 20:00:00', '2025-09-10 19:00:00', 'cloud://backup/1/5');

INSERT INTO `play_store`.`reviews` (`id`, `account_id`, `app_id`, `rating`, `comment`, `created_at`, `updated_at`) VALUES
(1,  11, 1,  5.0, 'Чудовий застосунок, користуюся щодня',   '2025-03-20 10:00:00', NULL),
(2,  12, 2,  4.5, 'Дуже зручний редактор',                  '2025-04-20 12:00:00', '2025-05-01 12:00:00'),
(3,  13, 3,  3.5, NULL,                                      '2025-05-20 09:00:00', NULL),
(4,  14, 4,  4.0, 'Розклад інколи запізнюється з оновленням', '2025-08-01 15:00:00', NULL),
(5,  15, 5,  2.5, 'Гра часто вилітає',                      '2025-08-25 18:00:00', '2025-09-05 18:00:00'),
(6,  11, 6,  4.8, 'Найкращий плеєр',                        '2025-09-10 11:00:00', NULL),
(7,  12, 8,  1.0, 'Забагато реклами',                       '2025-10-05 16:30:00', NULL),
(8,  13, 10, 3.0, NULL,                                      '2025-11-01 21:10:00', NULL),
(9,  14, 3,  0.0, 'Не запускається',                        '2025-11-03 10:40:00', NULL),
(10, 1,  5,  4.2, 'Цікавий сюжет',                          '2025-09-20 19:00:00', NULL);

COMMIT;