package com.ezio.framework.datasource;

import java.util.Map;
import javax.sql.DataSource;
import org.springframework.jdbc.datasource.lookup.AbstractRoutingDataSource;
import com.ezio.common.config.datasource.DynamicDataSourceContextHolder;
/**
 * @author admin
 * @version 1.0.0
 * @ClassName DynamicDataSource.java
 * @Description TODO
 * @createTime 2020年11月11日 17:16:00
 */
public class DynamicDataSource extends AbstractRoutingDataSource {
    public DynamicDataSource(DataSource defaultTargetDataSource, Map<Object, Object> targetDataSources)
    {
        super.setDefaultTargetDataSource(defaultTargetDataSource);
        super.setTargetDataSources(targetDataSources);
        super.afterPropertiesSet();
    }

    @Override
    protected Object determineCurrentLookupKey()
    {
        return DynamicDataSourceContextHolder.getDataSourceType();
    }
}
