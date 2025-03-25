SELECT p.descripcion as name,p.numero_ingredientes ,p.codigo,  ps.allergies_risk, ps.cancer_risk, ps.development_risk, ps.endocryne_risk, ps.env_risk, ps.prohibited_risk, p.score
 FROM productos p
INNER JOIN product_scores ps
ON p.id = ps.producto_id

