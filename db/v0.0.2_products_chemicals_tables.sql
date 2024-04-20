CREATE TABLE products (
    id uuid NOT NULL PRIMARY KEY DEFAULT gen_random_uuid(),
    barcode text,
    createdAt timestamp DEFAULT NOW()
);

CREATE TABLE chemicals (
    id uuid NOT NULL PRIMARY KEY DEFAULT gen_random_uuid(),
    createdAt timestamp DEFAULT NOW()
);

CREATE TABLE productsChemicals (
    productId uuid NOT NULL REFERENCES products(id),
    chemicalId uuid NOT NULL REFERENCES chemicals(id),
    createdAt timestamp DEFAULT NOW(),
    PRIMARY KEY (productId, chemicalId)
);

CREATE TABLE productTranslations (
    id uuid NOT NULL REFERENCES products(id),
    language text NOT NULL, -- from https://en.wikipedia.org/wiki/IETF_language_tag
    isDefault boolean NOT NULL,
    name text NOT NULL,
    createdAt timestamp DEFAULT NOW()
);

CREATE TABLE chemicalTranslations (
    id uuid NOT NULL REFERENCES chemicals(id),
    language text NOT NULL, -- from https://en.wikipedia.org/wiki/IETF_language_tag
    isDefault boolean NOT NULL,
    name text NOT NULL,
    score int,
    createdAt timestamp DEFAULT NOW()
);

CREATE TABLE chemicalDetails (
    id uuid NOT NULL REFERENCES chemicals(id),
    details text,
    source text,
    createdAt timestamp DEFAULT NOW()
);

-- DROP TABLE chemicalDetails;
-- DROP TABLE chemicalTranslations;
-- DROP TABLE productTranslations;
-- DROP TABLE productsChemicals;
-- DROP TABLE chemicals;
-- DROP TABLE products;


-- Example
-- 1. Insert product
INSERT INTO products (createdAt) VALUES (NOW());
INSERT INTO productTranslations (id, language, isDefault, name)
    VALUES ((SELECT id FROM products ORDER BY createdAt DESC LIMIT 1), 'en', true, 'Olaplex Hair Perfector No. 3 Repairing Treatment');

-- 2. Insert two chemicals
INSERT INTO chemicals (createdAt) VALUES (NOW());
INSERT INTO chemicalTranslations (id, language, isDefault, name)
    VALUES ((SELECT id FROM chemicals ORDER BY createdAt DESC LIMIT 1), 'en', true, 'Propylene Glycol');
INSERT INTO productsChemicals (productId, chemicalId)
    VALUES ((SELECT id FROM products ORDER BY createdAt DESC LIMIT 1), (SELECT id FROM chemicals ORDER BY createdAt DESC LIMIT 1));
-- (run the rest of the code in a separate run)
INSERT INTO chemicals (createdAt) VALUES (NOW());
INSERT INTO chemicalTranslations (id, language, isDefault, name)
    VALUES ((SELECT id FROM chemicals ORDER BY createdAt DESC LIMIT 1), 'en', true, 'Cetearyl Alcohol');
INSERT INTO productsChemicals (productId, chemicalId)
    VALUES ((SELECT id FROM products ORDER BY createdAt DESC LIMIT 1), (SELECT id FROM chemicals ORDER BY createdAt DESC LIMIT 1));

-- 3. Display result
SELECT pt.id AS productId, pt.language AS productLanguage, pt.name AS productName, pt.createdAt AS productCreatedAt, 
    ct.id AS chemicalId, ct.language AS chemicalLanguage, ct.name AS chemicalName, ct.createdAt AS chemicalCreatedAt FROM products p
INNER JOIN productTranslations pt ON p.id = pt.id
INNER JOIN productsChemicals pc ON p.id = pc.productId
LEFT JOIN chemicals c ON pc.chemicalId = c.id
INNER JOIN chemicalTranslations ct ON c.id = ct.id
